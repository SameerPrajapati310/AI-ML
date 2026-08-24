#include <bits/stdc++.h>
using namespace std;

class DepositeAccount{
    public:
        virtual void deposit(double amount) = 0;
};

class WithdrawAccount : public DepositeAccount{
    public:
        virtual void withdraw(double amount) = 0;
};

class SavingsAccount : public WithdrawAccount{
    private:
        double amount;
    public:
        SavingsAccount( double amount){
            this->amount = amount;
        }
        void deposit(double amt) override{
            amount += amt;
        }
        void withdraw(double amt) override{
            amount -= amt;
        }
};

class CurrentAccount : public WithdrawAccount{
    private:
        double amount;
    public:
        void deposit(double amt) override{
            amount += amt;
        }
        void withdraw(double amt) override{
            amount -= amt;
        }
};

