<p align="center">
  <a href="https://opensea.io/collection/willow-away">
    <img src="https://github.com/will7hughes/OpenSeaUploader/blob/main/cover_uploader.jpg" width="100%" />
  </a>
</p>

# OpenSea Uploader
A bulk uploader for uploading NFTs to OpenSea using Selenium, Excel, VBA, and Python.
  
# Support the Author
Want to support the author?<br>
Check out their OpenSea Collection: https://opensea.io/collection/willow-away<br>
Paypal: https://paypal.me/willowaway<br>
Venmo: @Willow_Hughes
Wallet Address: <B>0xC2229aD79F60526CaD49629200584a81cC1B1b28</b><br>

## Support the Co-Author
This project has a large amount of code from the GitHub author <b>karakule3dfx</b>. <br>
This project would not have been possible without their source code that I used as a basis for this script. <br>
So if you like this script, show them some love and give em a tip.<br>
The code was modified and updated with features to match my needs.<br><br>
If you want to support them, buy them a coffee ;)<br>
GitHub link: https://github.com/karakule3dfx<br>
OpenSea Collection Link: https://opensea.io/collection/fortune-cat-neko<br>
Paypal: https://paypal.me/klvntss<br>
Ethereum address: 0xd5146965809e4286e24dcf2bfbf58c3840d433a2<br>

# Disclaimer
This script does not collect or scrape any information while it is running.<br>
It is a good idea to look at the code yourself and understand the program before running it or modifying it.<br>
We will not be liable for any losses and/or damages for using our script. <br>
<b>Use at your own risk</b>

# Instructions
<ul>
  <li>Download and extract this project in your local device (Read the code before running. Do not modify until you understand the script)</li>
  <li>Download and update Python. My python version is <b>3.10</b></li>
  <li>Download your compatible chromedriver.exe https://chromedriver.chromium.org/downloads</li>
  <li>Extract and copy the chromedriver.exe and replace the chromedriver.exe in the "projects directory/chromedriver.exe"
  <li>Put all the NFTs images into folder “src/images” (etc 1.png), and NFTs properties metadata .json file put into folder src/json. (etc 1.json)</li>
  <li>Open this project folder with any code editor and open "Powershell " or "Terminal"</li>
  <li>Pip install requirements.txt by running the following command (pip install -r requirements.txt) <br>
    Please install PIP for Python if “pip is not recognized as an internal or external command</li>
  <li>Run the script, type "python upload.py"</li>
  <li>Once running the script, will pop-up the application </li>
  <li>Fill in the form for your project upload properties, </li>
  <ul>
    <li>Opensea collection link: https://www.opensea.io/collection/yourcollectionsname/<b>assets/create</b></li>
    <li>Opensea collection link must end with "assets/create", <br>
    look like this : https://www.opensea.io/collection/yourcollectionsname/<b>assets/create</b></li>
    <li>Start number 1</li>
    <li>End number 9999 or any number</li>
    <li>Default price: 0.02 (Will only be used if you do not specify in the .json file)</li>
    <li>NFT image format "png"</li>
    <li>External link start with http….</li>
  </ul>
  <li>Click and Select the “src” folder.</li>
  <li>Double check your image / json format: 1.png or 1.json</li>
  <li>Double check your json format: Refer to sample json file in /references/sample.json</li>
  <li>If Polygon please tick "Polygon Blockchain</li>
  <li>Please check "Complete Listing" for <b>listing for sale</b> OR unchecked "complete listing" for just creating the NFT</li>
  <li>Click and “Save this Form”</li>
  <li>Click “Open Chrome Browser” will popup a new chrome browser, Download metamask extension if haven't already.</li>
  <li>Login to your metamask account.</li>
  <li>Disable OpenSea Night Mode</li>
  <li>Download I'm not robot captcha clicker, extension link: https://chrome.google.com/webstore/detail/im-not-robot-captcha-clic/ceipnlhmjohemhfpbjdgeigkababhmjc/related?hl=en-US</li>
  <li>Download Buster, Captcha Solver, extension link: https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en-US</li>
  <li>Allow Chrome Extension Permissions and <b>Run</b> if prompted</li>
</ul>

# Chrome Extension, Under Development, Not Ready for Use!
Install the OpenSea Uploader Chrome Extension<br>
* chrome://extensions<br>
* Expand the Developer dropdown menu and click “Load Unpacked Extension”<br>
* Navigate to this projects folder directory/chrome_extension<br>
* Click Ok<br>
* To run, click the extension and click "Upload NFTs"<br>
<br>

## Install the following extensions<br>
* I'm not a robot captcha click: https://chrome.google.com/webstore/detail/im-not-robot-captcha-clic/ceipnlhmjohemhfpbjdgeigkababhmjc<br>
* Buster Captcha Solver: https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en-US<br>

## Version Log
<ul>
  <li><b>Version 1.0.3</b><br>
      Added executible<br>
  </li>
  <li><b>Version 1.0.2</b><br>
      Cleaned up code<br>
  </li>
  <li><b>Version 1.0.1</b><br>
      Added form validation<br>
  </li>
  <li><b>Version 1.0.0</b><br>
      Initial version. Upload your preconfigured img and json files in the src directory.<br>
  </li>
</ul>

# Message for a MacOS user
Currently this script only tested in Windows 10. Not compatible for MacOS. Subject to change in the future. Send me an email <b>willowawaymarket@gmail.com</b>
If you'd like to see a MacOS version in the future.

# Contact me
If you have any questions or want to get in contact you can email me at willowawaymarket@gmail.com or message me on social media's listed below<br>
* Twitter: https://twitter.com/willow_away<br>
* Instagram: https://www.instagram.com/willow_away/<br>
* Reddit: https://www.reddit.com/user/WillowAwayArt<br>

# Thanks
Please share, favorite, and leave a <b>star</b> on the repo.<br>
If you found it useful, you can leave a tip. I would greatly appreciate the support. <br>
Paypal: https://paypal.me/willowaway<br>
Venmo: @Willow_Hughes<br>
Wallet Address: <b>0xC2229aD79F60526CaD49629200584a81cC1B1b28</b><br>
Thank you, I hope you find this tool useful. </p>
