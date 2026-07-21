import asyncio


from app.ai.kernel import AIKernel

from app.agents.manager import ManagerAgent



async def main():


    kernel = AIKernel()


    manager = ManagerAgent()


    kernel.register_manager(

        manager

    )


    result = await kernel.execute(

        """
Создай калькулятор.

Он должен быть интерактивным.
Нужны графики функций.
Нужна визуализация решения.
Сделай архитектуру как для настоящего приложения.
"""

    )


    print()

    print("================")

    from app.helpers.display import print_result

    print_result(result)

    print("================")



asyncio.run(main())
