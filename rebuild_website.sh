#!/bin/bash

# TODO 
# attention probleme de git pull, de build (shopt not found)
# besoin de loop sur tous les book.toml
# bien faire les ln avec les scripts et les media sur tous les dossiers dans book/
# revoir les ./../media (qui ne marchent pas en local de toute facon) dans les fichier md > media/
# build depuis la machine ubuntu pour faire des build test en local
# créer la version francaise et tester la redirection de langue (la page doit exister, obligatoire)

#installation des packages requis
python3 -m pip install beautifulsoup4 lxml --no-input

# ---------------------------------------------------------------
# variables declaration
root_dir=${PWD}

# ---------------------------------------------------------------
# PRE BUILD SCRIPTS
echo "[ PRE-BUILD PART ]"
# python pre process scripts
cd ${root_dir}/scripts

# set the hall of fame in .mb
python3 -m hall_of_fame.py || true
# set the links in .mb
python3 -m link_md.py || true
# build the requirement tests result md page
python3 -m test-results.py || true
# update the glossary to each src/**/*.md page
python3 -m glossary.py || true
# update the variables values to each src/**/*.md page
python3 -m variables.py || true
# update the summary to each src/**/*.md page
python3 -m page-summary.py || true
# improve the lisibility of important words
python3 -m highlight-terms.py
# improve the lisibility of [[actions]]
python3 -m highlight-actions.py || true
# replace png images with jpg lighter ones
python3 -m png-to-jpg.py || true

cd ${root_dir}

# save previous build
rm -rf ${root_dir}/book.previous_build
mv ${root_dir}/book ${root_dir}/book.previous_build

# ---------------------------------------------------------------
# BUILD SCRIPTS
echo "[ BUILD PART ] "
# find all the book.toml files and execute the build
for folder in $(find src -type d);
do
    # si le dossier courant contient le fichier book.toml, alors build du book
    if [ -f "${folder}/book.toml" ]; then
        echo mdbook build ${root_dir}/${folder} -d ${root_dir}/${folder/src/book}
        mdbook build ${root_dir}/${folder} -d ${root_dir}/${folder/src/book}
    fi
done

# ---------------------------------------------------------------
# POST BUILD SCRIPTS
echo "[ POST-BUILD PART ]"

# remove unneccessary output folders (https:)
for folder in $(find book -type d);
do
    foldername=$(basename $folder)
    if [[ "${foldername}" == "https:" ]] || [[ "${foldername}" == "http:" ]]; then
        rm -rf "${folder}"
    fi
done

# python post process scripts
cd ${root_dir}/scripts

# all of the html pages are created, we can build the sitemap
python3 -m generate_sitemap.py || true
# add the dropdown "Version" on each book/**/*.html page generated by mdbook
# python3 -m version.py || true
# add the dropdown "Language" on each book/**/*.html page generated by mdbook
# python3 -m language.py || true
# add css link
python3 -m custom-css.py || true
# add css link
python3 -m custom-js.py || true
# update the navigation summary
python3 -m nav-summary.py || true
# update the requirements tests results format for PASS, FAIL and NOT_TESTED cells
python3 -m test-results-format.py || true
## update summary title and subtitle
python3 -m summary_title.py || true
# update the rating system
python3 -m rating.py || true
# fix link format (remove '.html' endings for external links) on each book/**/*.html page generated by mdbook
python3 -m link.py  || true # must be after rating to prevent the top title to have a subtitle "user find this page useful !"
# update the home page
python3 -m home.py || true
# update the dev team page
python3 -m dev_team.py || true
# update the roadmap page
python3 -m roadmap.py || true
# update lets make a game page
python3 -m lets_make_a_game.py || true
# update installation page
python3 -m installation.py || true
# update rpg power forge overview page
python3 -m overview.py || true
# update the footer part
python3 -m footer.py || true
# update community join button
python3 -m join-community.py || true
# update devlog embedded videos
python3 -m devlogs.py || true

# HERO PAGE ADDITION HERE
# add hero page
cp ${root_dir}/resources/hero.html ${root_dir}/book/index.html
# add links for home page to work (assuming we have /doc at least)
ln -s ${root_dir}/book/doc/css ${root_dir}/book/css
ln -s ${root_dir}/book/doc/FontAwesome ${root_dir}/book/FontAwesome
ln -s ${root_dir}/book/doc/fonts ${root_dir}/book/fonts

# add link thumbnails
#python3 -m thumbnail.py
# update favicons
python3 -m favicon.py || true

cd ${root_dir}

## zip user manual resources files
cd ${root_dir}/media/
zip -r user_resources.zip user_resources

cd ${root_dir}

# process remaining output folders
for folder in $(find book -type d);
do
    # process folder
    # add folders links (css, js, media, ...)
    ln -s ${root_dir}/media/ ${root_dir}/${folder}/media
    ln -s ${root_dir}/custom-js/ ${root_dir}/${folder}/custom-js
    ln -s ${root_dir}/custom-css/ ${root_dir}/${folder}/custom-css
done

# ---------------------------------------------------------------
# WEBSITE METADATA
# Now the website is built, we can add metadata files
# robots.txt
cp ${root_dir}/resources/robots.txt ${root_dir}/book/robots.txt

# ---------------------------------------------------------------
# LARGE FILE DOWNLOAD
echo "[ GIT LFS CHECKOUT PART ] "
cd ${root_dir}
# define $HOME for the user (www-data) 
export HOME=/home/www-data
git lfs install --force && git lfs fetch && git lfs checkout
