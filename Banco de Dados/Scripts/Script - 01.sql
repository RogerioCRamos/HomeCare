SELECT
	tb_visitamedica.cod_visita,
    tb_visitamedica.nome_medico,
    tb_especialidade.especialidade,
    tb_visitamedica.observacoes
FROM
    tb_visitamedica
INNER JOIN
    tb_especialidade ON tb_visitamedica.cod_especialidade = tb_especialidade.cod_especialidade
WHERE
    tb_visitamedica.dt_saida is null
