//2nd Degree Equation Calculator
//rezolva ecuatii de gradul 2s
#include <iostream>
#include <cmath>
using namespace std;
int main(){
    float a,b,c,d,x1,x2;
    cout << "introdu a,b,c: " ;
    cin >>a>>b>>c;
    d=pow(b,2)-(4*a*c);
    if(d<0){
        cout<<"delta < 0, ecuatia nu are soultie";
    }else if(d==0){
        cout<<"delta = 0"<<endl;
        x1= -b/(2*a);
        cout <<"S={("<<x1<<")}";
    }else if(d>0){
    cout << "delta= "<<d<<endl;
    x1=(-b-sqrt(d))/(2*a);
    cout <<"X1= "<<x1<<endl;
    x2=(-b+sqrt(d))/(2*a);
    cout <<"X2= "<<x2<<endl;
    cout <<"S={("<<x1<<";"<<x2<<")}";
    }
    return 0;
}
