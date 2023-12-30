#!/bin/bash

# TODO
# attention probleme de git pull, de build (shopt not found)
# besoin de loop sur tous les book.toml
# bien faire les ln avec les scripts et les media sur tous les dossiers dans book/
# revoir les ./../media (qui ne marchent pas en local de toute facon) dans les fichier md > media/
# build depuis la machine ubuntu pour faire des build test en local
# créer la version francaise et tester la redirection de langue (la page doit exister, obligatoire)

# ---------------------------------------------------------------
# variables declaration
root_dir=${PWD}

# ---------------------------------------------------------------
# PRE BUILD SCRIPTS
echo "[ PRE-BUILD PART ]"
# python pre process scripts
cd ${root_dir}/scripts

# build the requirement tests result md page
python3 -m test-results.py
# update the glossary to each src/**/*.md page
python3 -m glossary.py
# update the summary to each src/**/*.md page
python3 -m page-summary.py
# improve the lisibility of important words
python3 -m highlight-terms.py
# improve the lisibility of [[actions]]
python3 -m highlight-actions.py

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
# add the dropdown "Version" on each book/**/*.html page generated by mdbook
python3 -m version.py
# add the dropdown "Language" on each book/**/*.html page generated by mdbook
python3 -m language.py
# fix link format (remove '.html' endings for external links) on each book/**/*.html page generated by mdbook
python3 -m link.py
# add css link
python3 -m custom-css.py
# add css link
python3 -m custom-js.py
# update the navigation summary
python3 -m nav-summary.py
# update the requirements tests results format for PASS, FAIL and NOT_TESTED cells
python3 -m test-results-format.py
# update the rating system
python3 -m rating.py
# update the home page
python3 -m home.py
# update the dev team page
python3 -m dev_team.py
# update lets make a game page
python3 -m lets_make_a_game.py
# update the footer part
python3 -m footer.py

# HERO PAGE ADDITION HERE
# add hero page
cp ${root_dir}/resources/hero.html ${root_dir}/book/index.html
# add links for home page to work (assuming we have /en/stable at least)
ln -s ${root_dir}/book/en/stable/css ${root_dir}/book/css
ln -s ${root_dir}/book/en/stable/FontAwesome ${root_dir}/book/FontAwesome
ln -s ${root_dir}/book/en/stable/fonts ${root_dir}/book/fonts

# add link thumbnails
python3 -m thumbnail.py
# update favicons
python3 -m favicon.py

cd ${root_dir}




# add redirection in every language root folder (book/*/)
for folder in $(ls -d book/*);
do
    if [ -d "${folder}" ]; then
        cp ${root_dir}/resources/redirect_to_stable.html ${root_dir}/${folder}/index.html
    fi
done

# process remaining output folders
for folder in $(find book -type d);
do
    # process folder
    # add folders links (css, js, media, ...)
    ln -s ${root_dir}/media/ ${root_dir}/${folder}/media
    ln -s ${root_dir}/custom-js/ ${root_dir}/${folder}/custom-js
    ln -s ${root_dir}/custom-css/ ${root_dir}/${folder}/custom-css
done