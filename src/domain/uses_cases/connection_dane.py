from src.domain.uses_cases.authentication_use_cases import AuthenticationUseCase
from typing import List


class ConnectionDane:
    @staticmethod
    async def table_price(token: str) -> List[dict]:
        validate_token = await AuthenticationUseCase.get_user_current(token)
        if validate_token is True:
            return [
                {
                  'numero': 1,
                  'fecha': '19/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Tomate',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 2,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Platano',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 3,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Ahuyama',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 4,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Cebolla',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 5,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Cebollin',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 6,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Cilantro',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 7,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Papa',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 8,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Platano',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 9,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Arveja',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 10,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Frijol',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 11,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Lenteja',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 12,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Pepino',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 13,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Yuca',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 14,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Maiz',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
                {
                  'numero': 15,
                  'fecha': '20/11/2023',
                  'fuente': 'Corabastos',
                  'articulo': 'Pimenton',
                  'promedio': 2000,
                  'minimo': 1500,
                  'maximo': 2500
                },
              ]
