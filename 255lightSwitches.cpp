#include <iostream>
#include <fstream>

int main(int argc, char* argv[])
{

	std::ifstream infile(argv[1]);

	int nbSwitches;
	int k,debut,fin;
	infile >> nbSwitches;
	bool etatSwitches[nbSwitches];
	for (k = 0; k < nbSwitches; k++){
		etatSwitches[k] = 0;
	}



	while(infile >> debut >> fin)
	{
		if (debut < fin)
		{
			for (k=debut;k<=fin;k++)
			{
				etatSwitches[k] = !etatSwitches[k];
			}

		}

		else
		{
			for (k=debut;k>=fin;k--)
			{
				etatSwitches[k] = !etatSwitches[k];
			}

		}


	}


	int nbAllumes = 0;
	for (k = 0; k < nbSwitches; k++){
		nbAllumes = nbAllumes + (int)(etatSwitches[k]);
	}


	std::cout << "Nombre de lampes allumees : " << nbAllumes <<"\n";

	return(0);
}