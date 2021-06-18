# DS4A_Project
DS4A Capstone Project


NOTE: this only looks at actor/actress/support (actors/actress)/director nominees. This is a small portion of the kaggle nominee dataset from kaggle.

#scripts running steps

1. run get_bacon_kaggle_conflict_names.py
This will take the raw the_oscar_award.csv from https://www.kaggle.com/unanimad/the-oscar-award and spit out names that dont match in the oracle of bacon website using the "check_name_exists_on_bacon" method. Use that ouput and edit the csv manually to add a second column with the spelling as it is recommended in the oracle of bacon website. Then run the last function "fix_problem_names" to get the oracle of bacon spelling version of the nominees kaggle dataset

2. run clean_bacon_data.py (a handful of people go missing in the output, needs work)
This will take the bacon dataset from https://oracleofbacon.org/data.txt.bz2
and the new "the_oscar_award_corrected.csv" output from the previous step and 
spits out a dataframe of every movie the nominee has been in (according to the bacon dataset)

'''
title	year	role	name
The Birth of a Nation	1915	star	Lillian Gish
The Birth of a Nation	1915	cast	Donald Crisp
Blade Runner	1982	star	Harrison Ford
Blade Runner	1982	star	Edward James Olmos
Blade Runner	1982	director	Ridley Scott
'''


3. run create_node_edges_nominees.py (might need to reformat nodes output and possibly reformat it, needs work)
This will take in the output from step 3 and 
and create two csvs one for edges and one for nodes

bacon_edges.csv
'''
               source              target
0        Lillian Gish        Donald Crisp
1       Harrison Ford  Edward James Olmos
2       Harrison Ford        Ridley Scott
3  Edward James Olmos        Ridley Scott
4         Gene Wilder       Madeline Kahn
'''

bacon_nodes.csv ( this is only one row output, probably not the best way to format this)

'''
name	films
Lillian Gish	{'The Birth of a Nation': ('star', 1915), 'Broken Blossoms': ('star', 1919), 'The Night of the Hunter (film)': ('star', 1955), 'The Wind (1928 film)': ('star', 1928), 'Duel in the Sun (film)': ('cast', 1946), 'Intolerance (film)': ('star', 1916), 'The Whales of August': ('star', 1987), 'A Wedding': ('star', 1978), 'Ben-Hur: A Tale of the Christ (1925 film)': ('cast', 1925), 'Portrait of Jennie': ('cast', 1948), 'Warning Shot (1967 film)': ('star', 1967), 'The Unforgiven (1960 film)': ('cast', 1960), 'Follow Me, Boys!': ('star', 1966), 'Judith of Bethulia': ('cast', 1914), 'Way Down East': ('star', 1920), 'Hearts of the World': ('star', 1918), 'One Romantic Night': ('star', 1930), 'Orphans of the Storm': ('star', 1921), 'The New York Hat': ('star', 1912), 'Annie Laurie (1927 film)': ('star', 1927), 'The Green-Eyed Devil': ('cast', 1914), 'Home, Sweet Home (1914 film)': ('star', 1914), 'The Hunchback (1914 film)': ('star', 1914), 'An Unseen Enemy': ('star', 1912), 'Oil and Water (film)': ('cast', 1913), 'Sweet Liberty': ('star', 1986), 'Commandos Strike at Dawn': ('star', 1942), 'Two Daughters of Eve': ('cast', 1912), 'So Near, yet So Far': ('cast', 1912), 'In the Aisles of the Wild': ('star', 1912), 'The One She Loved': ('cast', 1912), 'The Painted Lady': ('cast', 1912), 'Gold and Glitter': ('cast', 1912), 'The Informer (1912 film)': ('cast', 1912), 'Brutality (film)': ('cast', 1912), "The Burglar's Dilemma": ('cast', 1912), 'A Cry for Help (1912 film)': ('cast', 1912), 'The Unwelcome Guest': ('cast', 1913), 'The Left-Handed Man': ('star', 1913), 'A Modest Hero': ('cast', 1913), 'Madonna of the Storm': ('star', 1913), 'The Battle at Elderbush Gulch': ('star', 1913), 'Lord Chumley': ('star', 1914), 'La BohÃ¨me (1926 film)': ('star', 1926), 'My Baby (film)': ('cast', 1912), 'A Misunderstood Boy': ('cast', 1913), 'The Lady and the Mouse': ('star', 1913), 'The House of Darkness': ('cast', 1913), 'Just Gold': ('cast', 1913), 'A Timely Interception': ('cast', 1913), 'The Mothering Heart': ('cast', 1913), 'During the Round-Up': ('star', 1913), "An Indian's Loyalty": ('star', 1913), 'A Woman in the Ultimate': ('star', 1913), 'So Runs the Way': ('star', 1913), 'The Conscience of Hassan Bey': ('star', 1913), 'The Battle of the Sexes (1914 film)': ('star', 1914), 'The Quicksands': ('star', 1914), 'The Rebellion of Kitty Belle': ('star', 1914), 'The Angel of Contention': ('star', 1914), "Man's Enemy": ('star', 1914), 'The Tear That Burned': ('star', 1914), 'The Folly of Anne': ('star', 1914), 'The Sisters (1914 film)': ('star', 1914), 'The Lost House': ('star', 1915), 'Enoch Arden (1915 film)': ('star', 1915), 'Captain Macklin': ('star', 1915), 'The Lily and the Rose': ('star', 1915), 'Pathways of Life': ('star', 1916), 'Daphne and the Pirate': ('star', 1916), 'Sold for Marriage': ('star', 1916), 'An Innocent Magdalene': ('star', 1916), 'Diane of the Follies': ('star', 1916), 'The Children Pay': ('star', 1916), 'The House Built Upon Sand': ('star', 1916), 'Souls Triumphant': ('star', 1917), 'The Great Love (1918 film)': ('star', 1918), 'Lillian Gish in a Liberty Loan Appeal': ('star', 1918), 'The Greatest Thing in Life': ('star', 1918), 'A Romance of Happy Valley': ('star', 1919), 'The Greatest Question': ('star', 1919), 'The White Sister (1923 film)': ('star', 1923), 'Romola (film)': ('star', 1924), 'The Scarlet Letter (1926 film)': ('star', 1926), 'The Enemy (1927 film)': ('star', 1927), 'Orders to Kill': ('star', 1958), 'His Double Life': ('star', 1933), "Miss Susie Slagle's": ('star', 1946), 'Remodeling Her Husband': ('director', 1920), 'Hambone and Hillie': ('star', 1984)}
'''

4. run bacon_nominees_network.py (needs work)
This will help create the network graph using the node, edges csv.
Having this data in graph format might help us think about how the connections/attributes relate to winning an award.
