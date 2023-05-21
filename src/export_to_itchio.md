# Export your game to itch.io

This section covers the export of a game made with **RPG Power Forge** to itch.io (an online plateform and marketplace for game developpers)

To export your game to itch.io, you will need an itch.io project first.

---
## Create a project on itchio

Go to https://itch.io. In the top-right corner of the webpage, select [Register]

![register.png](./../media/export_itchio/register.png)

Fill the form and login to your new account.

### Verify your mail adress

Once logged in, go to your profile settings and ask for a verification.

![verify.png](./../media/export_itchio/verify.png)

> 🐲 You won't be able to export your game from **RPG Power Forge** to itchio if you don't verify your mail adress first.

### Create a new project

Go to your dashboard (https://itch.io/dashboard) and select [Create new project].

![create_new_project.png](./../media/export_itchio/create_new_project.png)

Fill the form accordingly :
* Title : whatever you like
* Project URL : autofill from Title field, but you can edit it if you like
* Short desctription : optional oneliner.
* Classification : **Game**
* Kind of project : **HTML**

> 🐲 The project URL is important because it will be used by **RPG Power Forge** to find it on itch.io.

![project_settings.png](./../media/export_itchio/project_settings.png)

Hit [Save]. Your project is ready !

---
## Export your game to itchio

Go back in **RPG Power Forge**. As you can see, I have an awesome map to export.

![export_scene.png](./../media/export_itchio/export_scene.png)

Choose [Build for Web] in the drop-down menu.

![build_for_web.png](./../media/export_itchio/build_for_web.png)

You are prompted with the Export UI.

![export_web_build_settings.png](./../media/export_itchio/export_web_build_settings.png)

Property|Type|Function|Example
--------|--------|--------|--------
Version|Integers|The version (Major.Minor.Patch) of your game | 0.0.1
Product Name|String|Name of your game (no space)| My_awesome_game
Company Name|String|Name of your company| My awesome company
Directory|Selector|Path of the output folder where the game is built (no space)| C:/output

> 🐲 **Product Name** and **Directory** must not have spaces !

Additionnaly, you can export your game to itch.io with the following properties.

![export_web_creds.png](./../media/export_itchio/export_web_creds.png)

Property|Type|Function|Example
--------|--------|--------|--------
Upload to itch.io|Checkbox|Whenever you want you game to be upload to itch.io| ☑️
Account Name|String|Name of your itch.io account. If your profile page is https://gif-superretroworld.itch.io, then your account name is **gif-superretroworld**| gif-superretroworld
Project Name|String|Name of your itch.io project. If your project page is https://gif-superretroworld.itch.io/rpg-power-forge-export, then your project name is **rpg-power-forge-export**| rpg-power-forge-export
Channel Name|String|A tag for your itch.io project (no space)| web


> 🐲 **Account Name** and **Project Name** fields are mandatory to perform the upload correctly ! On the first export you will be asked to link **RPG Power Forge** with **itch.io**. Click [Create] to do so (the web browser opens : connect to your itch.io account and authorise "butler", the itch.io game uploader).

![export_web_authorize.png](./../media/export_itchio/export_web_authorize.png)

When everything is set, you can click [Build].

![export_web_build.png](./../media/export_itchio/export_web_build.png)

When the export is done, you can see logs in the Console Window, telling your game has been uploaded.

![export_build_success.png](./../media/export_itchio/export_build_success.png)

Itch.io webpage also notifies you.

![itchio_notification.png](./../media/export_itchio/itchio_notification.PNG)

Congratulation, your game is now online ! Test my sample map here : https://gif-superretroworld.itch.io/rpg-power-forge-export?secret=d2TMyzQ8Ero5Kblk8OEx9WgMp0