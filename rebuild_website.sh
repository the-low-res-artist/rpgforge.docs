# TODO
# attention probleme de git pull, de build (shopt not found)
# besoin de loop sur tous les book.toml
# bien faire les ln avec les scripts et les media sur tous les dossiers dans book/
# revoir les ./../media (qui ne marchent pas en local de toute facon) dans les fichier md > media/
# build depuis la machine ubuntu pour faire des build test en local
# créer la version francaise et tester la redirection de langue (la page doit exister, obligatoire)

# ---------------------------------------------------------------
# variables
root_dir=${PWD}

# ---------------------------------------------------------------
# PRE BUILD SCRIPTS
echo "[ PRE-BUILD PART ] "
# update the glossary to each src/**/*.md page
cd ${root_dir}/scripts && python3 -m glossary.py && cd ${root_dir}

# save previous build
mv ${PWD}/book ${PWD}/book.previous_build

# ---------------------------------------------------------------
# BUILD SCRIPTS
echo "[ BUILD PART ]"
# find all the book.toml files and execute the build
for folder in $(find src -type d);
do
    # si le dossier courant contient le fichier book.toml, alors build du book
    if [ -f "${folder}/book.toml" ]; then
        mdbook build ${PWD}/${folder} -d ${PWD}/${folder/src/book}
    fi
done

# remove unneccessary output folders (https:)
for folder in $(find book -type d);
do
    foldername=$(basename $folder)
    if [[ "${foldername}" == "https:" ]] || [[ "${foldername}" == "http:" ]]; then
        rm -rf "${folder}"
    fi
done

# process remaining output folders
for folder in $(find book -type d);
do
    # process folder
    # add js + media links
    ln -s ${PWD}/media/ ${PWD}/${folder}/media
    ln -s ${PWD}/js/ ${PWD}/${folder}/js
done

#shopt -s globstar
#for i in src/**/book.toml; do # Whitespace-safe and recursive
#    filepath="$i"
#    src_folderpath=${root_dir}/$(dirname "${filepath}")
#    dest_folderpath=${src_folderpath/src/book}
#    echo ==========================================================
#    echo mdbook build ${src_folderpath} -d ${dest_folderpath}
#    mdbook build ${src_folderpath} -d ${dest_folderpath}
#    ln -s ${root_dir}/media/ ${root_dir}/book/en/stable/media
#    ln -s ${root_dir}/scripts/ ${root_dir}/book/en/stable/js
#done

# ---------------------------------------------------------------
# POST BUILD SCRIPTS
echo "[ POST-BUILD PART ]"
# add the dropdown "Version" on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m version.py && cd ${root_dir}
# add the dropdown "Langage" on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m langage.py  && cd ${root_dir}
# fix link format (remove '.html' endings for external links) on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m link.py  && cd ${root_dir}