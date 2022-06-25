from pympler import tracker

def send_email():
    return 'Email sent!'

def main():
    tr = tracker.SummaryTracker()

    result = send_email()
    print(result)

    tr.print_diff()

if __name__ == "__main__":
    main()
