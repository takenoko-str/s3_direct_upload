from flask import Flask, render_template, request, redirect, url_for
from botocore.client import Config
import os, json, boto3
import random
import datetime

app = Flask(__name__)

def s3_prefix(key):
    prefix = str(hex(random.randint(16, 255)))
    time = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    return os.path.join(prefix + '-' + time, key)

@app.route("/")
def hello():
    return "hello world"

@app.route("/account/")
def account():
    return render_template('account.html')

@app.route("/submit_form/", methods = ["POST"])
def submit_form():
  username = request.form["username"]
  full_name = request.form["full-name"]
  avatar_url = request.form["avatar-url"]
  #DB登録処理は割愛
  #update_account(username, full_name, avatar_url)

  return redirect(url_for('account'))

@app.route('/sign-s3/', methods=["GET", "POST"])
def sign_s3():
    S3_BUCKET = os.environ.get('S3_BUCKET', 'your-s3-bucket-name')

    file_name = request.args.get('file-name')
    file_type = request.args.get('file-type')
    # If your bucket is in a region that requires a v4 signature, then you can modify your boto3 client configuration to declare this
    s3 = boto3.client('s3', region_name='ap-northeast-1',
                      config=Config(signature_version='s3v4'))

    presigned_post = s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl": "public-read", "Content-Type": file_type},
        Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn = 3600
    )
    print("*", presigned_post)

    return json.dumps({
        'data': presigned_post,
        'url': 'https://{}.s3.amazonaws.com/{}'.format(S3_BUCKET, file_name)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.debug = True
    app.run(host='0.0.0.0', port = port)

