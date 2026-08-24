#include<bits/stdc++.h>
using namespace std;

class Product{
    public:
        string name;
        double price;
    public:
        Product( string name, double price ){
            this->name = name;
            this->price = price;
        }
};

class ShoppingCart{
    private:
        vector<Product*> products;
    public:
        void add_to_cart(Product* p){
            products.push_back(p);
        }
        const vector<Product*>& get_product(){
            return products;
        }
        double calculateTotal(){
            double total = 0;
            for ( auto p : products ){
                total += p->price;
            }
            return total;
        }
};

class getInvoice{
    private:
        ShoppingCart* cart;
    public:
        getInvoice(ShoppingCart* cart){
            this->cart = cart;
        }
        void generateInvoice(){
            double total = cart->calculateTotal();
            cout << "Invoice generated. Total: " << total << endl;
        }
};

class SavetoDB{
    private:
        ShoppingCart* cart;
    public:
        virtual void save(ShoppingCart* cart) = 0;
};

class SaveToFile : public SavetoDB{
        void save(ShoppingCart* cart) override {
        cout << "Saving shopping cart to SQL DB!!!" << endl;
    }
};

class SaveToCloud : public SavetoDB{
        void save(ShoppingCart* cart) override {
        cout << "Saving shopping cart to cloud storage..." << endl;
    }
};

int main(){
    ShoppingCart* cart = new ShoppingCart();
    Product* p1 = new Product("laptop",100.112);
    cart->add_to_cart(p1);
    Product* p2 = new Product("mouse",12345.098);
    cart->add_to_cart(p2);

    getInvoice* invoice = new getInvoice(cart);
    invoice->generateInvoice();

    SavetoDB* dbSaver = new SaveToFile();
    dbSaver->save(cart);

    dbSaver = new SaveToCloud();
    dbSaver->save(cart);

    delete p1;
    delete p2;
    delete cart;
    delete invoice;
    delete dbSaver;

    return 0;
}