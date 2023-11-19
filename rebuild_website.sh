# TODO attention probleme de git pull, de build (shopt not found)

# ---------------------------------------------------------------
# variables
root_dir=${PWD}

# ---------------------------------------------------------------
# PRE BUILD SCRIPTS

# update the glossary to each src/**/*.md page
cd ${root_dir}/scripts && python3 -m glossary.py && cd ${root_dir}

# ---------------------------------------------------------------
# BUILD SCRIPTS
# find all the book.toml files and execute the build
mdbook build /var/www/com.rpgforge/public/src/en/stable -d /var/www/com.rpgforge/public/book/en/stable
ln -s /var/www/com.rpgforge/public/media/ /var/www/com.rpgforge/public/book/en/stable/media
ln -s /var/www/com.rpgforge/public/scripts/ /var/www/com.rpgforge/public/book/en/stable/js

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

# add the dropdown "Version" on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m version.py && cd ${root_dir}
# add the dropdown "Langage" on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m langage.py  && cd ${root_dir}
# fix link format (remove '.html' endings for external links) on each book/**/*.html page generated by mdbook
cd ${root_dir}/scripts && python3 -m link.py  && cd ${root_dir}