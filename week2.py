def main():
    response = input("How happy are you from 1-10")
    howMany = int(response)
    smiles = "\U0001F600 \n\ "*howMany
    print(smiles)

main()

