### s3_direct_upload
Flaskでs3にダイレクトにアップロードするHerokuのチュートリアルを参考に
### やったこと
- S3上でバケットを作成し、CORSを設定する
- EC2上にgunicornとnginxの環境を構築
- venvでpythonの環境を構築し、ファイルをデプロイする
- DNSで特定のドメインにELBのエンドポイントを設定する（その他セキュリティ周りの設定）
- 画像をアップロード

### 参考URL
- https://devcenter.heroku.com/articles/s3-upload-python
- https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
