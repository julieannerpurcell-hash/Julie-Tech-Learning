using System;

public class BankAccount
{
    public string Owner { get; set; }
    public decimal Balance { get; private set; }

    public BankAccount(string owner, decimal startingBalance = 0)
    {
        Owner = owner;
        Balance = startingBalance;
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0) { Console.WriteLine("Deposit must be positive."); return; }
        Balance += amount;
        Console.WriteLine($"Deposited {amount:C}. New balance: {Balance:C}");
    }

    public void Withdraw(decimal amount)
    {
        if (amount > Balance) { Console.WriteLine("Insufficient funds."); return; }
        Balance -= amount;
        Console.WriteLine($"Withdrew {amount:C}. New balance: {Balance:C}");
    }

    static void Main(string[] args)
    {
        var account = new BankAccount("Julie", 100);
        account.Deposit(50);
        account.Withdraw(30);
    }
}