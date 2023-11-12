# move temporary to the script folder
cd scripts

# update the glossary to each src/*.md page
python3 -m glossary.py

# back to root folder
cd ..
