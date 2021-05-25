from app.models import db, Product


def seed_products():

    product1 = Product(
        sku='SS4MCOS',
        name='Striped socks',
        category_id=4,
        image_url='https://cdnd.lystit.com/photos/2012/04/16/paul-smith-multi-striped-socks-product-1-3276627-727547536.jpeg',
        description='socks, woolen',
        regular_price=8.00
    )

    db.session.add(product1)

    product2 = Product(
        sku='NS4BKOS',
        name='Neon socks',
        category_id=4,
        image_url='https://partycity6.scene7.com/is/image/PartyCity/_pdp_sq_?$_1000x1000_$&$product=PartyCity/592140',
        description='socks, cotton and fun!',
        regular_price=9.00
    )

    db.session.add(product2)

    product3 = Product(
        sku='PS4MCOS',
        name='Plaid socks',
        category_id=4,
        image_url='https://ae01.alicdn.com/kf/HTB1K.z2NFXXXXXJXXXXq6xXFXXXL/New-Autumn-Winter-Cotton-Dress-Socks-Mens-Crew-Socks-Business-Classic-Plaid-Socks-Fashion-Colorful-Leisure.jpg',
        description='Thick and stylish socks',
        regular_price=8.00
    )

    db.session.add(product3)

    product4 = Product(
        sku='WSG4BROS',
        name='Wayfair sunglasses',
        category_id=4,
        image_url='https://i.pinimg.com/originals/10/35/f4/1035f4ee12a0bb2aef446e0dd6422132.jpg',
        description='Wayfair brown sunglasses',
        regular_price=100.00
    )
    db.session.add(product4)

    product5 = Product(
        sku='ASG4TSOS',
        name='Aviator sunglasses',
        category_id=4,
        image_url='https://cdnc.lystit.com/photos/2012/05/09/persol-brown-plastic-aviator-sunglasses-product-2-3465708-409937962.jpeg',
        description='Aviator tortoise sunglasses',
        regular_price=75.00
    )
    db.session.add(product5)

    product6 = Product(
        sku='WHSG4WOS',
        name='White round sunglasses',
        category_id=4,
        image_url='https://www.topsunglasses.net/wp-content/uploads/2016/11/White-Round-Sunglasses-Pictures.jpg',
        description='White stylish round sunglasses with a flair',
        regular_price=35.00
    )
    db.session.add(product6)

    product7 = Product(
        sku='BB4BKOS',
        name='Black belt',
        category_id=4,
        image_url='https://www.thefashionisto.com/wp-content/uploads/2018/04/Salvatore-Ferragamo-2018-Mens-Switch-Belt-Style-001.jpg',
        description='Sleek black belt for any occasion',
        regular_price=35.00
    )
    db.session.add(product7)

    product8 = Product(
        sku='BRB4BROS',
        name='Brown Belt',
        category_id=4,
        image_url='https://i.etsystatic.com/5712391/r/il/1c329f/668497568/il_794xN.668497568_o38h.jpg',
        description='Simple rustic brown belt for any occasion',
        regular_price=20.00
    )
    db.session.add(product8)

    product9 = Product(
        sku='SSB4MCOS',
        name='Snake skin Be`lt',
        category_id=4,
        image_url='https://i.pinimg.com/originals/39/17/95/3917954d50ce0d7889dad4b9042e891d.jpg',
        description='Elegant and stylish snake skin belt for that chic look',
        regular_price=40.00
    )
    db.session.add(product9)

    product10 = Product(
        sku='BYB4YOS',
        name='Bright yellow Belt',
        category_id=4,
        image_url='https://i.pinimg.com/originals/d1/25/4d/d1254d703bb6f6a0c28f19f9fce5c620.jpg',
        description='Fashion forward with the utility looking style of a belt',
        regular_price=18.50
    )
    db.session.add(product10)

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()