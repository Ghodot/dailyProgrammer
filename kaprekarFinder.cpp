#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>



using namespace std;

bool is_kaprekar(int nombre)
{

	int part1,part2;
	string nombreString = to_string(nombre*nombre);
	int longueurNombre = nombreString.size();

	//cout << "Nombre etudie : " << nombre <<"\n" << "Son carre : "<<nombreString <<"\n";

	for (int k = 1;k < longueurNombre;k++)
	{
		part1 = atoi(nombreString.substr(0,k).c_str());
		part2 = atoi(nombreString.substr(k,longueurNombre).c_str());

		//cout << "Partie 1 : " << part1 <<" et partie 2 : " << part2 <<"\n";
		if(part1 + part2 == nombre and part2>0)
		{
			cout << nombre <<" ";
		}
	}





	return(1);

}


int main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout << "MERCI de rentrer 2 arguments, pas " << argc-1 << "\n";
	}

	int minimum = atoi(argv[1]), maximum = atoi(argv[2]);
	
	for (int k=minimum;k <= maximum;k++)
	{
		is_kaprekar(k);
	}

	cout <<"\n";

	return(0);




}