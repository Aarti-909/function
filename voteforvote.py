def eligible_for_vote(age):
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible")
eligible_for_vote(int(input("enter ur age-: ")))