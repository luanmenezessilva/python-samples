+----+--------+----------------------+
| id | id_pai | nome                 |
+----+--------+----------------------+
|  1 |      0 | A Empresa            |
|  2 |      1 | Sobre Nós            |
|  3 |      1 | Objetivos            |
|  4 |      3 | Objetivo dos nossos  |
|  5 |      0 | Contato              |
|  6 |      0 | Produtos             |
+----+--------+----------------------+

OU 

$cats[1]['id_pai'] = 0;
$cats[1]['nome'] = 'A Empresa';

$cats[2]['id_pai'] = 1;
$cats[2]['nome'] = 'Sobre Nós';

$cats[3]['id_pai'] = 1;
$cats[3]['nome'] = 'Objetivo';

$cats[4]['id_pai'] = 3;
$cats[4]['nome'] = 'Objetivos dos Nossos Clientes';

$cats[5]['id_pai'] = 0;
$cats[5]['nome'] = 'Contato';

$cats[6]['id_pai'] = 0;
$cats[6]['nome'] = 'Produtos';




----- FONTE ORIGINAL
/**
 * Função que monta o menu com as categorias e subcategorias.
 * @param id_pai ID da categoria pai cujas subcategorias serão buscadas.
 * @param ArrayCats Array com as categorias do menu.
*/

function montaMenu( $id_pai, $arrayCats ) {
    
	// calcula o número de índices do array
	$catsSize = count( $arrayCats );
 
	echo "<ul>";
 
	for ( $i = 1; $i <= $catsSize; $i++ )
	{
		if ( $arrayCats[ $i ]['id_pai'] == $id_pai )
		{
			echo "<li>";
			echo $arrayCats[ $i ]['nome'];
 
			// busca as subcategorias da categoria atual
			montaMenu( $arrayCats[ $i ]['id'], $arrayCats );
 
			echo "</li>";
		}
	}
	echo "</ul>";
}


----- OUTRA POSSIBILIDADE

function montaMenu( $id_pai, $arrayCats, $leftMost, $rightMost )
{
    echo "<ul>";

    for ( $i = $leftMost; $i < $rightMost; $i++ )
    {
        if ( $arrayCats[ $i ]['id_pai'] == $id_pai )
        {
            echo "<li>", $arrayCats[ $i ]['nome'],
            $leftMost++;
            montaMenu( $arrayCats[ $i ]['id'], $arrayCats, $leftMost, $rightMost );
            echo "</li>";
        }
    }
    echo "</ul>";
}