# weakest

# its life cycle is for one function call only and then it is thrown away.

class Printer:
    def printer(self):
        print("Printing.....")

class AnnualReport:
    def create_report(self):
        print("Creating an Anual report")
        printer = Printer()
        printer.printer()
        print("Report created !!!")

report = AnnualReport()
report.create_report()