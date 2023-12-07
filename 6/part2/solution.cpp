#include <iostream>
#include <fstream>
#include <string>
#include<vector>
using namespace std;

int main () {
  string line;
  ifstream myfile ("input.txt");
  if (myfile.is_open())
  {

    Vector<string> time;
    Vector<string> records;
    while(getline(myfile, line)) {
      char * ;
      pch = strtok(str," ,.-");
      while (pch != NULL)
      {
        printf ("%s\n",pch);
        pch = strtok (NULL, " ,.-");
      }
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}