# GitHub Webhook Body

You can integrate the <a href="https://api.spontit.com">Spontit API</a> with GitHub webhooks. For a video on how to do so, see <a href="https://youtu.be/nNa07pnQndM">here</a>.

To set up GitHub push notifications, see the steps below.

We use the function in `get_github_webhook_body.py` on our server to generate the body of the notification. 

If you use the Spontit API and want us to format the body differently, or improve the way we format the body and generate the description, simply <a href="https://github.com/spontit/github-webhook-string/compare" target="_blank">create a pull request</a> or <a href="https://github.com/spontit/github-webhook-string/issues/new" target="_blank">issue</a> and we'll review it. If it all checks out, we'll test it and update our server. 

We GREATLY appreciate all additions.

To set up GitHub push notifications, see the steps below.

1) Go to the repository you want notifications for. Go to "Settings". Go to "Webhooks". Click "Add Webook".
2) Sign up for Spontit at <a href="https://spontit.com">spontit.com</a>. Get the mobile app. Make sure notifications are turned on for both the website and the mobile app. Send a test notification and make sure it goes through. If you have any trouble, email info@spontit.com.
3) Go to the channel on Spontit that you want notifications sent to. You can view a list of your channels at <a href="https://spontit.com/push">spontit.com/push</a>. At that link, you can also create a channel.
4) Get the link of the channel you want to send your pushes to. You can get this link by selecting the channel on the "Push" tab and then selecting "View". Say your username is <b>fruits</b>. The link for your main channel is <a href="https://spontit.com/fruits">spontit.com/fruits</a>. If you create a channel called "Apple", then the link for that channel is called <a href="https://spontit.com/fruits/apple">spontit.com/fruits/apple</a>.
5) For the payload URL, enter https://api.spontit.com/webhooks/github/{channel_id} where <i>channel_id</i> is either <b>fruits</b> or <b>fruits/apple</b>, depending on the channel you chose (see Step #4). You can create an unlimited number of channels. Thus, if you chose the channel available at <a href="https://spontit.com/fruits/apple">spontit.com/fruits/apple</a>, then the final link would be https://api.spontit.com/webhooks/github/fruits/apple, for example. If you chose the channel available at <a href="https://spontit.com/fruits">spontit.com/fruits</a> (i.e. your main channel), then the final link would be https://api.spontit.com/webhooks/github/fruits.
6) Make sure "Content Type" is "application/json".
7) For the secret, go to <a href="https://spontit.com/secret_keys">spontit.com/secret_keys</a> and get a secret key. Copy and paste that key into the "Secret" box.
8) Enable SSL, select "Just the push event", check "Active", and click "Update Webhook". You should immediately get a notification on your devices. Sometimes Android phones might take a few minutes.
9) Invite others to your channel and to Spontit using the link in step #4!

If you have any trouble, please do not hesitate to reach out at info@spontit.com. We highly recommend watching the video tutorial <a href="https://youtu.be/nNa07pnQndM">here</a>.
