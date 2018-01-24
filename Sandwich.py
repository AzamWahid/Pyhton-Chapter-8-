def sandwich(sandwichname,*Want):
    print("\nMaking a "+sandwichname+" sandwich with following things:")
    for thing in Want:
        print("-"+thing)

sandwich('club','cheese')
sandwich('chicken','cheese','katchup')







