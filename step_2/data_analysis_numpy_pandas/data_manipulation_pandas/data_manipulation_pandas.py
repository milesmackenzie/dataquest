# reading food_info.csv and displaying columns in a list

import pandas

food_info = pandas.read_csv("food_info.csv")
col_names = food_info.columns.tolist()
print (col_names)
print (food_info.head(3))

# dividing and multipying values under Sodium_(mg) and Sugar_Tot_(g)

sodium_grams = food_info["Sodium_(mg)"] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000

# dividing and adding different columns to eachother in their respective rows

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]

# using non-calculated nutritional index of
# (Score = 2 * (Protein_(g)) - 0.75 * (Lipid_Tot_(g)))

weighted_protein = food_info["Protein_(g)"] * 2
weighted_fat = food_info["Lipid_Tot_(g)"] * -0.75
initial_rating = weighted_fat + weighted_protein

print (initial_rating)

# normalizing Protein_(g) and Lipid_Tot_(g) using .max() and dividing
# all values by the max

max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"]/max_protein

max_lipid = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"]/max_lipid

# normalizing data in Protein_(g) and Lipid_Tot_(g) and assigning names
# to Normalized_Fat and Normalized_Protien

normalized_protein = (food_info["Protein_(g)"] - food_info["Protein_(g)"].min()) / (food_info["Protein_(g)"].max() - food_info["Protein_(g)"].min())
normalized_fat = (food_info["Lipid_Tot_(g)"] - food_info["Lipid_Tot_(g)"].min()) / (food_info["Lipid_Tot_(g)"].max() - food_info["Lipid_Tot_(g)"].min())

food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

# creating new column showing nutritional index score:
# Score = 2 * (Protein_(g)) - 0.75 * (Lipid_Tot_(g)))

food_info["Norm_Nutr_Index"] = (2*normalized_protein) - (0.75*normalized_fat)

# sorting DataFrame in place rather than producing new one and
# returning in descending order

food_info.sort_values("Norm_Nutr_Index", inplace=True, ascending=False)
