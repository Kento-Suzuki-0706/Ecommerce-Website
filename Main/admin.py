from flask import Blueprint
from . import db
from .models import Category, Product, Order


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='Snowboard', image='category1.jpeg')
    category2 = Category(name='Bindings', image='category2.jpeg')
    category3 = Category(name='Boots', image='category3.jpeg')
    category4 = Category(name='Other Gears', image='category4.jpeg')
        
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.add(category4)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    p1 = Product(category_id=category1.id, image='snowboard1.jpeg', price=629.00,\
        name='BURTON Snowboard',\
        description= "Pro Calibre is a strong weapon for any board, but the Men's Burton Custom X Snowboard has repeatedly met the needs of the most demanding snowboarders with precision design and powerful glide. That confidence comes from tech features such as Squeeze Box High, a core profile with carbon for increased snap power, competition-grade base and 45° carbon highlights for lightness of response High Voltage. For hard riding, the Custom X board is available in two versions. Camber for power or Flying V for floating fun without edge snagging.") 
    p2 = Product(category_id=category1.id, image='snowboard2.jpeg', price=729.00,\
        name='SALOMON Snowboard',\
        description= 'The Wonder combines a directional twin shape with lockout camber for versatility on groomers and in powder. The medium directional flex and ghost basalt stringers provide the perfect balance between stability and playfulness. The cork damper also reduces the load on your feet and the environment.')
    p3 = Product(category_id=category1.id, image='snowboard3.webp', price=829.00,\
        name='CAPiTA Snowboard',\
        description= 'Focus on freeride ease of use. The tapered shape with a wide nose and narrow tail allows you to quickly switch edges and control the board in all conditions, whether it be rough terrain, powder or narrow tree runs. Equipped with a flex booster, the board can fly higher with less effort.')
    p4 = Product(category_id=category2.id, image='binding1.jpeg', price=689.00,\
        name='BURTON Bindings',\
        description= 'This features SpringBED suspension for superior response and a carbon composite Ultra Highback for professional handling. Designed for aggressive all-mountain riders and also features Zero Forward Lean for easy freestyle adjustment, the EST® version combines with the Burton Channel mounting system for the ultimate in flex and feel.')                
    p5 = Product(category_id=category2.id, image='binding2.jpeg', price=540.00,\
        name='SALOMON Bindings1',\
        description= 'The DISTRICT features SHADOW FIT technology for maximum freestyle performance on jumps, rails and side hits. The natural connection of the simple but soft heel cup improves binding and boot performance and comfort. The asymmetrical highback and newly adopted injection straps provide both support and manoeuvrability.')
    p6 = Product(category_id=category2.id, image='binding3.webp', price=799.00,\
        name='SALOMON Bindings2',\
        description= "The RHYTHM is a unisex model packed with features for a great fit and a comfortable ride, especially designed with the user's progression in mind and featuring flexibility to glide smoothly on uneven slopes: 3D SUPREME straps, full EVA footbed, asymmetrical highback. asymmetrical highback, to name but a few.")
    p7 = Product(category_id=category3.id, image='boots1.webp', price=789.00,\
        name='BURTON Boots',\
        description= 'Highest standards in every detail. With the now legendary Burton Aion BOA® snowboard boot, you can push as hard as you want on any mountain. One of the many high-tech features on board is the High Power Focus BOA® Fit System, which allows you to fine-tune the tension and feel of each of the two independent lacing zones to suit your riding style. The combination of heat-reflective foil and a moisture-wicking liner keeps your feet warm and dry by absorbing perspiration without allowing body heat to escape. The cushioning is excellent and conforms to your feet even when new, allowing for a relaxed, natural stance to ride over any terrain.')
    p8 = Product(category_id=category3.id, image='boots2.webp', price=699.00,\
        name='SALOMON Boots1',\
        description= 'Soft flex / Characteristics include manoeuvrability at low speeds and a high tolerance for board \'shake\' that can occur in a variety of situations. Recommended for snowboard beginners, freestyle training and riders who want to play with the board like a skateboard.')
    p9 = Product(category_id=category3.id, image='boots3.webp', price=629.00,\
        name='SALOMON Boots2',\
        description= 'For riders like Danny Davis looking for high performance and full-grain leather style, we\'ve combined waterproof leather with the trademark functionality that made this boot legendary. Aion\'s proven design creates a relaxed, natural stance that allows for thread-stitching turns and stable landings rarely seen on snowboards. The lightweight, heat-mouldable liner keeps feet warm and dry all day with heat-reflecting, sweat-wicking technology for a comfortable fit.')
    p10 = Product(category_id=category4.id, image='clothes.jpeg', price=499.00,\
        name='BURTON Snowboarding Clothes',\
        description= 'Lightweight and comfortable to wear. Insulated snowboarding clothing that releases sweat quickly and keeps body heat in, making it comfortable and easy to move around in on the snowy slopes. It is warm and breathable and designed to be lightweight and easy to pack for backcountry riding. The stretch fabric is lightweight and breathable, allowing for natural movement. Midweight layer for cold windy days and when climbing mountains. Wear it under a shell for warmth when skiing downhill. When the sun shines and temperatures rise, it can be easily stowed in the pocket.')
    p11 = Product(category_id=category4.id, image='goggle.jpeg', price=249.00,\
        name='SALOMON Goggle',\
        description= 'Precise, unmatched fit with polarised lenses that reduce glare. In short, it offers the clearest and widest field of vision possible. Furthermore, the magnetic lens change system allows you to quickly change lenses for a variety of conditions.')
    p12 = Product(category_id=category4.id, image='globes.jpeg', price=89.00,\
        name='BURTON Globes',\
        description= 'Insulated waterproof shell with leather palm. Comfortable riding. Warmer. The Burton Treeline mitten keeps you dry and lets you ride longer with less basics. Durable leather palm and waterproof shell with full insulation. Keeps your hands warm and protected for long days in the mountains. Touchscreen compatible so you can operate your mobile phone without having to remove your gloves and bare hands, and the pre-curved fit provides a natural fit and grip.')
    
    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.add(p9)
        db.session.add(p10)
        db.session.add(p11)
        db.session.add(p12)
        db.session.commit()
    except:
        return 'There was an issue adding a product in dbseed function'

    return 'DATA LOADED'


