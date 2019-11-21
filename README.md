# lineMessage

## clone project
```
git clone https://github.com/welch79328/lineMessage.git

pip install -r requirements.txt
```

## Write Channel access token
```
vim lineMessage/app/__config__.py
```

## deploy ubuntu-18.04 apache
```
#install apache
sudo apt-get update
sudo apt-get install apache2 -y

#install mod_wsgi
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo a2enmod wsgi

#vim 000-default.conf
<VirtualHost *:80>
    ServerName lineMessage
    WSGIScriptAlias / /var/www/lineMessage/flaskapp.wsgi
    <Directory /var/www/lineMessage/app/>
        Order allow,deny
        Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo service apache2 restart
```
