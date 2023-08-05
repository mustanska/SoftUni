from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}
    VALID_CLIENTS_LOANS = {"Student": "StudentLoan", "Adult": "MortgageLoan"}

    def __init__(self, capacity: int):
        self.capacity = capacity    # The number of clients а Bank can have
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if self.VALID_CLIENTS_LOANS[client.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")

        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                current_loan_interest = loan.interest_rate
                loan.increase_interest_rate()

                if current_loan_interest != loan.interest_rate:
                    number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                current_client_interest = client.interest
                client.increase_clients_interest()

                if current_client_interest != client.interest:
                    changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        not_granted_sum  = sum([l.amount for l in self.loans])
        total_interest_rate = 0

        for client in self.clients:
            total_clients_income += client.income
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += sum([l.amount for l in client.loans])
            total_interest_rate += client.interest

        avg_client_interest_rate = total_interest_rate / len(self.clients) if self.clients else 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
