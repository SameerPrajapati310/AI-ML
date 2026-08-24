#include <bits/stdc++.h>
using namespace std;

class Product {
private:
    string name;
    double price;
public:
    Product(string name, double price) {
        this->name = name;
        this->price = price;
    }
    string getName() const { return name; }
    double getPrice() const { return price; }
};

class ShoppingCart {
public:
    vector<Product*> products;

    void addProduct(Product* p) {
        products.push_back(p);
    }

    const vector<Product*>& getProducts() {
        return products;
    }

    double getTotalPrice() {
        double total = 0;
        for (auto p : products) {
            total += p->getPrice();
        }
        return total;
    }
};

class GetInvoice {
private:
    ShoppingCart* cart;
public:
    GetInvoice(ShoppingCart* cart) {
        this->cart = cart;
    }

    void PrintInvoice() {
        cout << "Printing Invoice:" << endl;
        for (const auto& p : cart->getProducts()) {
            cout << "Product Name: " << p->getName()
                 << ", Price: " << p->getPrice() << endl;
        }
        cout << "Total Price: " << cart->getTotalPrice() << endl;
    }
};

class StoringTodatabase {
private:
    ShoppingCart* cart;
public:
    StoringTodatabase(ShoppingCart* cart) {
        this->cart = cart;
    }
    void saveToDatabase() {
        cout << "Saving shopping cart to database..." << endl;
    }
};

int main() {
    ShoppingCart* cart = new ShoppingCart();
    cart->addProduct(new Product("Laptop", 50000));
    cart->addProduct(new Product("Mouse", 2000));

    GetInvoice* printer = new GetInvoice(cart);
    printer->PrintInvoice();

    StoringTodatabase* db = new StoringTodatabase(cart);
    db->saveToDatabase();

    return 0;
}



// StackMemory

// cart    -> 0x1000   (pointer to ShoppingCart on heap)
// printer -> 0x3000   (pointer to GetInvoice on heap)
// db      -> 0x4000   (pointer to StoringTodatabase on heap)


// HeapMemeory

// 0x1000 -> ShoppingCart
//            └── vector<Product*> products
//                  [0] -> 0x2000
//                  [1] -> 0x2010

// 0x2000 -> Product { name="Laptop", price=50000 }
// 0x2010 -> Product { name="Mouse",  price=2000 }

// 0x3000 -> GetInvoice { cart=0x1000 }

// 0x4000 -> StoringTodatabase { cart=0x1000 }
