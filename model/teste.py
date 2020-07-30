parser = argparse.ArgumentParser(prog='CARINA_LEGADO',
                                     description=_DESCRICAO,
                                     # epilog=cli.EPILOGO,
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     # parents=[cli.default_parser()]  # Parâmetros padrões do Alice
                                     )
                                                                                    'ser executado.')
    subparsers = parser.add_subparsers(help='sub-command help')
    # create the parser for the "pub" command
    parser_pub= subparsers.add_parser('pub', help='publicacao help')
    parser_pub.add_argument('-rdw', action="store_true", default=False, dest='reprocessar_download')
    parser_pub.add_argument('-rz', action="store_true", default=False, dest='reprocessar_extracao_zip')
    parser_pub.add_argument('-rp', action="store_true", default=False, dest='reprocessar_extracao_pub')
    parser_pub.add_argument('-dr', action="store", default=2, dest='dias_retroativos', type=int)
    # create the parser for the "disp_inex" command
    parser_disp_inex = subparsers.add_parser('disp_inex', help='disp_inex help')
    parser_disp_inex.add_argument('-rdi', action="store_true", default=False, dest='reprocessar_extracao')
    parser_disp_inex.add_argument('-dum', action="store", default=3, dest='dia_util_envio_email_mensal', type=int)
    parser_disp_inex.add_argument('--ano-mes', dest='ano_mes', action="store", nargs=2,
                        help='Determina o ano mês da planilha mensal a ser enviada')
    # create the parser for the "secao3" command
    parser_secao3 = subparsers.add_parser('secao3', help='secao3 help')
    # parser_secao3.add_argument('--baz', choices='XYZ', help='baz help')
    parser_secao3.add_argument('-rdi', action="store_true", default=False, dest='reprocessar_extracao')
    parser_secao3.add_argument('-dum', action="store", default=3, dest='dia_util_envio_email_mensal', type=int)
    parser_secao3.add_argument('--ano-mes', dest='ano_mes', action="store", nargs=2,
                        help='Determina o ano mês da planilha mensal a ser enviada')
    args = parser.parse_args()