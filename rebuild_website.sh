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
rm -rf ${PWD}/book.previous_build
mv ${PWD}/book ${PWD}/book.previous_build

# ---------------------------------------------------------------
# BUILD SCRIPTS
echo "[ BUILD PART ] "
# find all the book.toml files and execute the build
for folder in $(find src -type d);
do
    # si le dossier courant contient le fichier book.toml, alors build du book
    if [ -f "${folder}/book.toml" ]; then
        echo mdbook build ${PWD}/${folder} -d ${PWD}/${folder/src/book}
        mdbook build ${PWD}/${folder} -d ${PWD}/${folder/src/book}
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
# update favicons
python3 -m favicon.py
# update the navigation summary
python3 -m nav-summary.py
# update the requirements tests results format for PASS, FAIL and NOT_TESTED cells
python3 -m test-results-format.py
# update the rating system
python3 -m rating.py
# update the home page
#python3 -m home.py
cd ${root_dir}

# add home page
cp ${PWD}/resources/index.html ${PWD}/book/index.html

# add links for home page to work (assuming we have /en/stable at least)
ln -s ${PWD}/book/en/stable/css ${PWD}/book/css
ln -s ${PWD}/book/en/stable/FontAwesome ${PWD}/book/FontAwesome
ln -s ${PWD}/book/en/stable/fonts ${PWD}/book/fonts
ln -s ${PWD}/book/en/stable/ayu-highlight.css ${PWD}/book/ayu-highlight.css
ln -s ${PWD}/book/en/stable/highlight.css ${PWD}/book/highlight.css
ln -s ${PWD}/book/en/stable/tomorrow-night.css ${PWD}/book/tomorrow-night.css

# add redirection in every language root folder (book/*/)
for folder in $(ls -d book/*);
do
    if [ -d "${folder}" ]; then
        cp ${PWD}/resources/redirect_to_stable.html ${PWD}/${folder}/index.html
    fi
done

# process remaining output folders
for folder in $(find book -type d);
do
    # process folder
    # add folders links (css, js, media, ...)
    ln -s ${PWD}/media/ ${PWD}/${folder}/media
    ln -s ${PWD}/custom-js/ ${PWD}/${folder}/custom-js
    ln -s ${PWD}/custom-css/ ${PWD}/${folder}/custom-css
done