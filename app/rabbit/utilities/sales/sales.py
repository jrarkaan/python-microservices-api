from pkg.rabbit.model.entity import RabbitMQ


def SalesRabbitMQ():
    exchangeSalesName: str = "EthicalSales"
    kindOfExchange: str = "fanout"
    routingKey: str = "ethical_sales_gt_upsert"
    queueName: str = "ethical_sales_gt_upsert"

    SalesEthicalRabbit = RabbitMQ
    SalesEthicalRabbit.Exchange.Name = exchangeSalesName
    SalesEthicalRabbit.Exchange.KindOfExchange = kindOfExchange
    SalesEthicalRabbit.Exchange.BindingKey = routingKey
    SalesEthicalRabbit.Exchange.ConsumerTag = ""
    SalesEthicalRabbit.Exchange.Durable = True
    SalesEthicalRabbit.Exchange.AutoDelete = False
    SalesEthicalRabbit.Exchange.Internal = False
    SalesEthicalRabbit.Exchange.NoWait = False
    SalesEthicalRabbit.Exchange.Arguments = None
    SalesEthicalRabbit.Exchange.Mandatory = False
    SalesEthicalRabbit.Exchange.Immediate = False

    SalesEthicalRabbit.Queue.Name = queueName
    SalesEthicalRabbit.Queue.Durable = False
    SalesEthicalRabbit.Queue.AutoDelete = False
    SalesEthicalRabbit.Queue.Exclusive = False
    SalesEthicalRabbit.Queue.NoWait = False
    SalesEthicalRabbit.Queue.Arguments = None
    SalesEthicalRabbit.Queue.PrefetchCount = 1
    SalesEthicalRabbit.Queue.PrefetchSize = 0
    SalesEthicalRabbit.Queue.PrefetchGlobal = False

    SalesEthicalRabbit.Consume.AutoAck = True
    SalesEthicalRabbit.Consume.Exclusive = False
    SalesEthicalRabbit.Consume.NoWait = False
    SalesEthicalRabbit.Consume.NoLocal = False
    SalesEthicalRabbit.Consume.Arguments = None
