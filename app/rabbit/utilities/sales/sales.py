from pkg.rabbit.model.entity import RabbitMQ


def SalesRabbitMQ() -> RabbitMQ:
    exchangeSalesName: str = "EthicalSales"
    kindOfExchange: str = "fanout"
    routingKey: str = "ethical_sales_gt_upsert"
    queueName: str = "ethical_sales_gt_upsert"

    SalesEthicalRabbit = RabbitMQ(
        exchange={
            'Name': exchangeSalesName,
            'KindOfExchange': kindOfExchange,
            'BindingKey': routingKey,
            'ConsumerTag': "",
            'Durable': True,
            'AutoDelete': False,
            'Internal': False,
            'NoWait': False,
            'Arguments': None,
            'Mandatory': False,
            'Immediate': False,
        },
        queue={
            'Name': queueName,
            'Durable': False,
            'AutoDelete': False,
            'Exclusive': False,
            'NoWait': False,
            'Arguments': None,
            'PrefetchCount': 1,
            'PrefetchSize': 0,
            'PrefetchGlobal': False,
        },
        consume={
            'AutoAck': False,
            'Exclusive': False,
            'NoWait': False,
            'NoLocal': False,
            'Arguments': None
        },
    )

    return SalesEthicalRabbit