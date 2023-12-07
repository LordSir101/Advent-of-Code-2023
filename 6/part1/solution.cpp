#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include<vector>
#include <stdio.h>
#include <string.h>
#include <math.h>  
using namespace std;

int main () {
  string line;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {

    vector<int> times;
    vector<int> records;
    int line_num = 1;
    while(getline(myfile, line)) {
      std::string token = line.substr(line.find(":") + 1, line.size());
      //cout << token << endl;
      std::istringstream iss{ token};
      int number;
      if(line_num == 1){
          while(iss >> number){
              times.push_back(number);
          }
      }
      else{
           while(iss >> number){
              records.push_back(number);
          }
      }
        
        line_num++;
    }
    
    // use quadratic formula to fin roots when y = record + 1
    int total = 1;
    for(int i = 0; i < times.size(); i++){
        int a = -1;
        int b = times[i];
        int c = (records[i]+1) * -1;
        
        float dis = sqrt(pow(b,2) - (4*a*c));
        
        float r1 = (-1*b+ dis) / 2*a;
        float r2 = (-1*b - dis) / 2*a;
        
        int lowest = ceil(min(r1,r2));
        int highest = floor(max(r1,r2));
        
        int diff = highest - lowest;
        total *= diff + 1;
    }
    cout << total << endl;
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
    