# python-scripts-to-send-email-using-gmail-api
Python scripts to send email using Gmail API which helps you to save cost and time on your email campaign and have a higher chance of landing email into inbox.

### Prerequisites

```
Python 2.7.14
```

```
pip 9.0.3
```
### Installing [Steps to run script]



```
pip install httplib2
pip install oauth2client
pip install apiclient
pip install --upgrade google-api-python-client
pip install --upgrade python-gflags
```

### Steps to generate the API to access gmail.

```
1. You need a google account - either google apps or gmail. So, if you haven't got one, go get one.
2. Get yourself to the [developers console](https://console.developers.google.com)
3. Create a new project, and wait few seconds for that to complete.
4. Navigate to API's and Auth -> Credentials
5. Under OAuth select Create New Client ID
6. Choose Installed Application as the application type **Other**
7. You should now have a button Download JSON. Do that. It's your client_secret.json—the passwords so to speak
8. copy downloaded client_secret.json into credentials.json
```

## Running the script

```
python send-email.py --noauth_local_webserver
```


### After running the script console will ask you to enter the verification code

Below one is just a demo please go through the link given in your console

>https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose&redirect_uri=urnAoaut2.0%3Aoob&response_type=code&client_id=clientid.apps.googleusercontent.com&access_type=offline

>Enter verfication code:


> Please copy the link and enter in the browser then allow your Gmail account to give access to your application

> And then copy the verification code into console then click enter your email will be sent and

> It creates a gmail.storage file in your project directory which will have a token to send text emails without verification code.



## Author

* **Ravishankar S R** - *Full stack developer* - ravishankarsr.rav@gmail.com

* [Twitter](https://twitter.com/ravishankar_rav)
* [LinkedIn](https://www.linkedin.com/in/ravishankarsr-rav)


## License

MIT.
