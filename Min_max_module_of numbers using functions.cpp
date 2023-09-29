#include <iostream>
using namespace std;

int max(int, int);
int modul(int);
float min(float, float, float);
int main(){
int a,b,c;
float x;
cout << "a="; cin >>a;
cout << "b="; cin >>b;
cout << "c="; cin >>c;
cout << "max(" << a << "," << b << ")=" << max(a,b) <<
endl;
cout << "|"<< a+b+c << "|=" << modul(a+b+c)<< endl;
x=min(float(a)/b , float(b)/c, float(c)/a);
cout << "min=" << x<< endl;
}
int max(int a, int b){
    if (a>b) return a;
    else return b;
}
int modul(int x){
return (x>0)?x:-x;
}
float min(float x, float y, float z){
    if (x<y) return (x<z)?x:z;
    else return (y<z)?y:z;
}