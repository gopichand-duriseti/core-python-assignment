def ratings(feedback):
    if not feedback:
        print("No Ratings Given")
    else:
        if 4 in feedback or 5 in feedback:
            print(f'Positive Feedback:{(feedback.count(4)+feedback.count(5))/len(feedback)*100}%')
ratings([5, 4, 3, 5, 2, 4, 1, 5])
