# move temporary to the script folder
pushd ./scripts

# update the glossary to each src/*.md page
python3 -m glossary.py

# back to root folder
popd