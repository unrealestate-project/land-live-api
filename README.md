# Land Live+ MVP (Django Backend)

👋 Welcome to Land Corporation's first MVP!

This is a **Minimal Viable Product (MVP)** that consists of `reservation system` and `KakaoTalk notification` features along with visual guide line to help users understand the work flow. Main purpose of this MVP is to **_test whether there exists market needs for live-streaming tour for Real Estate_** while investing as minimum development as possible.

> Note that this is a MVP which does not contain any **real-time streaming** feature. Actual real-time streaming feature will be developed on next cycle; prototyping.

<p><br></p>

## Background

Please refer **[here](https://github.com/Land-Corporation/land-live-web#background)**

<p><br></p>

## Installation

Use the package manager [yarn](https://yarnpkg.com/) to install land-live-web

```bash
pip install -r requirements
```

<p><br></p>

## Usage

```bash
python manage.py migrate
python manage.py runserver
```

And open `http://localhost:8000/`

<p><br></p>

## Look & Feel

To see how it looks, please visit 👉 **[landcorp.io](https://landcorp.io)**

<p align="center">
  <img src="https://github.com/Land-Corporation/land-live-web/blob/devel/photo/landing_page.png" width="100%" title="hover text">
</p>

<p><br></p>

## Troubleshooting

<details>
<summary>1. Mysql Insert throws error when sending emoji in POST payload</summary>
<p>

#### Problem
```python3
    err.raise_mysql_exception(self._data)
  File "/Users/jinj/.virtualenvs/landapp/lib/python3.7/site-packages/pymysql/err.py", line 107, in raise_mysql_exception
    raise errorclass(errno, errval)
django.db.utils.DataError: (1366, "Incorrect string value: '\\xF0\\x9F\\x98\\x8A\\xF0\\x9F...' for column 'content' at row 1")
```

#### Solution
* MySQL DB Setting
  * utf8mb4_unicode_ci, utf8mb4

<p align="center">
  <img src="https://github.com/Land-Corporation/land-live-api/blob/master/photo/mysql_emoji.png" width="70%" title="hover text">
</p>

* Table Setting
  * Room
  * Feedback
`ALTER TABLE <table_name> CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;`

* Django Setting
```python3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True, },
    }
```
</p>
</details>

<details>
<summary>2. AWS ElasticBeanstalk: Custom Domain + HTTPS setting</summary>

#### Background
After done with AWS EB basic setup, url will look like `http://land-liveplus-env-prod.ap-northeast-2.elasticbeanstalk.com/`.
This is the url with no TLS enabled that AWS just assigned.

We Need to apply custom domain + TLS enabled like `https://api.landcorp.io`, `https:/dev-api.landcorp.io`

#### Solution

* (Prerequisite) EB + PostgreSql (not decoupled) Setup Complete
* Custom Domain `record routing setup`
  * https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-beanstalk-environment.html#routing-to-beanstalk-environment-create-resource-record-set
  * Since we can use `Region` (if using the latest EB) alias can be mapped
  * Create `hosted zone` at `Route53`
    * dev-api.landcorp.io --> A type
    * ElasticBeanstalk's existing URL as `value`
  * (if already done, skip) Change Name Servers in Google Domains to that of Route53
    * https://stackoverflow.com/questions/43402925/how-to-use-google-domain-on-elastic-beanstalk
  * Check `dev-api.landcorp.io`
    * Need to wait for about 30mins
* HTTPS Setup
Please refer https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html
  * Register wildcard certificate for at `certificate manager` (*.landcorp.io)
    * https://ap-northeast-2.console.aws.amazon.com/acm/home?region=ap-northeast-2#/firstrun/
    * both `landcorp.io`, `*.landcorp.io` need to be created
    * CNAME will be popped up. Just register to Route53 by clicking button.
  * In EB GUI, setup https listener in Application Load Balancer section
    * Please refer to the docs above
  * http → https redirect setup
    * https://aws.amazon.com/premiumsupport/knowledge-center/elb-redirect-http-to-https-using-alb/
    * Don't change at EB console. Please go to EC2 console, load balancer panel and change `Default Action`
* Success!

<p>
</details>


<details>
<summary>3. AWS ElasticBeanstalk: RDS for Production setup</summary>

<p>

#### Background
* EB+RDS automatic setup is not suitable for `production` mode.
* It isn't ideal for a production environment because it ties the lifecycle of the database instance to the lifecycle of your application's environment.

* You need to decouple RDS
This enables you to connect multiple environments to a database, terminate an environment without affecting the database, and perform seamless updates with blue-green deployments.


#### Solution
* Please refer to AWS docs
-> https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/rds-external-defaultvpc.html

* Create PostgreSql database
  * You will need to create only `default security group` but this will be changed soon
* Create new `Security Group`
  * Go to the newly created database, click `VPC security groups` in  `Security` tab
  * Below is the Inbound rules for automatically created of EB <> RDS. Refer this to make modification

<p align="center">
  <img src="https://github.com/Land-Corporation/land-live-api/blob/master/photo/inbound_rules.png" width="80%" title="hover text">
</p>

  * Please be cautious when setting up `Source`, numerous `Security groups` are located in one EB/EC2. Please refer to the existing Security groups of EC2 and their connection rule in `land-liveplus-env-dev` to configure.
    * In on sentence, just connect security group ID of EC2.
  * For `Type setting` ->  PostgreSql should be setup, not All TCP
  * Remove default in `RDS security group` and add new
* RDS security group → EB environment
  * Refer to the doc. Please be catious that this is to add existing RDS to security group
* Append RDS related environment variables
  * Please refer to the doc. Do it at `EB configuration`
* Done!

</p>

</details>


<p><br></p>

## Guide

Please refer **[here](https://github.com/Land-Corporation/land-live-web#guide)**

## Contributing

- All rights reserved to Land Corporation, Inc.
- Main developer: [@JinJis](https://github.com/JinJis)

<p><br></p>

## License

[MIT](https://choosealicense.com/licenses/mit/)
