import os
import re

cwd = "/Users/abdullahcakir/Desktop/viptrip"

contents = {
    "blog-esenboga-havalimani-vip-transfer-fiyatlari": """
    <h2>Esenboğa Havalimanı VIP Transfer Fiyatları ve Avantajları</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Ankara'ya seyahat edenler için <strong>Esenboğa VIP transfer</strong> hizmeti, standart ulaşım yöntemlerine göre çok daha konforlu bir alternatif sunmaktadır. 2026 yılı güncel transfer fiyatlarımız, sunduğumuz üst düzey <strong>şoförlü araç kiralama ankara</strong> standartlarına göre son derece uygundur.</p>
    <p>Bütçenizi sarsmadan, lüks ve prestijli bir yolculuk yapmak istiyorsanız, <strong>ankara havalimanı transfer</strong> paketlerimiz tam size göre. Fiyatlandırma politikamız sabit olup, sürpriz ücretlerle karşılaşmazsınız. Özel donanımlı araçlarımızla <strong>ankara vip transfer</strong> deneyimini en uygun fiyat garantisiyle yaşamak için bizimle hemen iletişime geçin.</p>
    """,
    "blog-esenboga-cankaya-vip-transfer": """
    <h2>Esenboğa'dan Çankaya'ya Lüks ve Kesintisiz Ulaşım</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Ankara'nın kalbi Çankaya'ya yapacağınız yolculuklarda <strong>esenboğa vip transfer</strong> servisimiz, yorgunluğunuzu unutturacak bir konfor sunar. İş toplantılarına veya evinize giderken <strong>ankara vip transfer</strong> ayrıcalığını hissetmek, seyahatinizin en keyifli kısmı olacak.</p>
    <p>Profesyonel ekibimiz, uçuşunuzu anlık olarak takip eder ve siz daha bagajınızı alırken kapıda sizi bekler. <strong>Ankara havalimanı transfer</strong> hizmetinde dakiklik ve güvenilirlik bizim için her şeyden önemlidir. Çankaya bölgesine <strong>şoförlü araç kiralama ankara</strong> hizmetimizle 7/24 VIP kalitesinde ulaşabilirsiniz.</p>
    """,
    "blog-esenboga-incek-vip-transfer": """
    <h2>Esenboğa - İncek Arası Şoförlü VIP Araç Kiralama</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Ankara'nın hızla gelişen ve lüks konut projeleriyle öne çıkan bölgesi İncek'e, <strong>esenboğa vip transfer</strong> hizmetimizle stressiz bir başlangıç yapın. Yüksek donanımlı <strong>mercedes vito kiralama</strong> filomuz sayesinde, yolda geçirdiğiniz zamanı dinlenerek değerlendirebilirsiniz.</p>
    <p>İncek bölgesindeki villalara, okullara veya iş merkezlerine özel <strong>ankara havalimanı transfer</strong> çözümlerimiz, tamamen size özel olarak planlanır. <strong>Şoförlü araç kiralama ankara</strong> arayışlarınızda, güler yüzlü personelimiz ve içecek ikramlarımızla VIP ulaşımın zirvesini yaşatıyoruz.</p>
    """,
    "blog-esenboga-golbasi-vip-transfer": """
    <h2>Esenboğa Havalimanı Gölbaşı VIP Transfer Hizmeti</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Gölbaşı'nın huzurlu atmosferine doğru yola çıkarken, <strong>esenboğa vip transfer</strong> farkıyla yolculuğunuzu taçlandırın. Filomuzda yer alan ultra lüks <strong>mercedes vito kiralama</strong> seçenekleriyle, tüm yol yorgunluğunuzu araç içinde bırakacaksınız.</p>
    <p>Trafik derdini düşünmeden arkanıza yaslanın; deneyimli şoförlerimiz sizi en güvenli rotalardan hedefinize ulaştırsın. <strong>Ankara havalimanı transfer</strong> hizmetlerimiz kapsamında sunduğumuz <strong>şoförlü araç kiralama ankara</strong> paketleri, Gölbaşı rotası için özel fiyat avantajlarına sahiptir.</p>
    """,
    "blog-esenboga-havalimani-luks-ulasim": """
    <h2>Esenboğa Havalimanı Lüks Ulaşım Çözümleri</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Başkentimize adım attığınız ilk andan itibaren <strong>esenboğa vip transfer</strong> ayrıcalığını yaşamak, iş seyahatlerinizin ve tatillerinizin kalitesini artırır. Filomuzun gözdesi olan <strong>mercedes vito kiralama</strong> hizmetimiz, misafirlerimize bir araçtan çok, yürüyen bir lüks ofis sunar.</p>
    <p>Yüksek standartlardaki <strong>ankara havalimanı transfer</strong> çözümlerimiz, televizyon, mini bar ve masajlı koltuk gibi donanımlarla yolculuğu bir keyif haline getirir. <strong>Şoförlü araç kiralama ankara</strong> ihtiyaçlarınızda, sıradan ulaşımların ötesine geçerek premium bir ulaşım deneyimi vadediyoruz.</p>
    """,
    "blog-esenboga-havalimani-karsilama-hizmeti": """
    <h2>Esenboğa CIP ve VIP İsimle Karşılama Hizmeti</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Sizleri veya yurt dışından gelen özel misafirlerinizi, Esenboğa Havalimanı çıkışında kişiselleştirilmiş <strong>esenboğa vip transfer</strong> tabelalarıyla karşılıyoruz. Amacımız, uçuş yorgunluğunuzu havalimanı kapısında sonlandırmaktır.</p>
    <p>Misafirleriniz için prestijin ne kadar önemli olduğunu biliyoruz. Bu yüzden <strong>ankara havalimanı transfer</strong> organizasyonlarımızda güler yüzlü, yabancı dil bilen şoförlerimizle hizmet vermekteyiz. En üst düzey <strong>şoförlü araç kiralama ankara</strong> deneyimi sunan karşılama hizmetimizle fark yaratıyoruz.</p>
    """,
    "blog-esenboga-transfer-mercedes-vito": """
    <h2>Esenboğa Transferinde Mercedes Vito Ayrıcalığı</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Havayolu yolculuğunuzun ardından konforlu bir başlangıç yapmak için <strong>mercedes vito kiralama</strong> tartışmasız en iyi seçenektir. Böylece <strong>ankara vip transfer</strong> süreciniz hem ferah hem de lüks bir ortamda geçer.</p>
    <p>Özel süspansiyon sistemleri ve ses yalıtımlı kabinleriyle, <strong>ankara havalimanı transfer</strong> güzergahında adeta süzülerek ilerleyeceksiniz. Tüm <strong>şoförlü araç kiralama ankara</strong> paketlerimizde standart olarak sunduğumuz VIP Vito serisi konforunuzu artırır.</p>
    """,
    "blog-ankara-esenboga-7-24-transfer": """
    <h2>Ankara Esenboğa 7/24 Kesintisiz VIP Transfer</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">VipTrip olarak <strong>esenboğa vip transfer</strong> hizmetimizi kesintisiz olarak 7 gün 24 saat sunuyoruz. Üstelik <strong>mercedes vito kiralama</strong> konforuyla gece yolculukları çok daha güvenli.</p>
    <p>Eğitimli ve dinamik şoför kadromuz sayesinde <strong>ankara havalimanı transfer</strong> ihtiyaçlarınız her zaman güvence altındadır. Ankara'nın her noktasına gece gündüz demeden sunduğumuz <strong>şoförlü araç kiralama ankara</strong> hizmetiyle, seyahat planlarınız asla yarıda kalmaz.</p>
    """,
    "blog-esenboga-vip-taksi-alternatifi": """
    <h2>Esenboğa Taksi Yerine VIP Transfer Neden Seçilmeli?</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Pek çok kişi havalimanı çıkışında ilk seçenek olarak taksiyi düşünse de, <strong>esenboğa vip transfer</strong> sunduğu avantajlarla çok daha mantıklı bir yatırımdır. Ayrıca bagaj sorunu yaşamadan, geniş <strong>mercedes vito kiralama</strong> araçlarında yolculuk yaparsınız.</p>
    <p>VIP araçlarımızda taksimetre stresi yoktur; ücret baştan bellidir. Ücretsiz Wi-Fi, su ve atıştırmalıklar <strong>ankara havalimanı transfer</strong> paketlerimize dahildir. Hem ekonomik hem de son derece prestijli bir <strong>şoförlü araç kiralama ankara</strong> hizmeti almak varken riske girmeyin.</p>
    """,
    "blog-esenboga-havalimani-soforlu-arac": """
    <h2>Esenboğa Havalimanı Şoförlü Araç Kiralama Rehberi</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Havalimanına indiğinizde sizi bir aracın bekliyor olması büyük bir lükstür. VipTrip, <strong>şoförlü araç kiralama ankara</strong> konusunda yılların tecrübesiyle misafirlerine güven vermektedir.</p>
    <p>Sunduğumuz <strong>mercedes vito kiralama</strong> seçenekleri, hem iş hem de tatil amaçlı gezilerinizde size prestij katar. Kapsamlı <strong>ankara havalimanı transfer</strong> rehberimizle tanışarak doğrudan lüksün keyfini çıkarabilirsiniz.</p>
    """,
    "blog-ankara-istanbul-vip-transfer": """
    <h2>Ankara İstanbul Arası VIP Transfer Konforu</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">İki büyük metropol arasındaki ulaşımı uçak veya otobüs çilesi çekmeden gerçekleştirmek istemez misiniz? <strong>Şehirler arası vip transfer</strong> hizmetimizle Ankara'dan İstanbul'a kapıdan kapıya premium yolculuk sunuyoruz.</p>
    <p>Günün istediğiniz saatinde mola verebilir, aracın arka kısmındaki VIP ofiste toplantılarınızı online olarak sürdürebilirsiniz. <strong>Şehirler arası transfer</strong> taleplerinizde uçağa binmek için havalimanında saatlerce beklemek yerine, <strong>şoförlü araç kiralama ankara</strong> servisimizle zamanınızı kendinize saklayın.</p>
    """,
    "blog-ankara-kapadokya-vip-transfer-rehberi": """
    <h2>Ankara'dan Kapadokya'ya VIP Transfer Rehberi</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Peri Bacaları'nın büyüleyici manzarasına doğru yola çıkarken, <strong>şehirler arası vip transfer</strong> ayrıcalığını VipTrip ile yaşayın. Geniş panoramik camlı <strong>mercedes vito kiralama</strong> araçlarımızla yolculuk yapabilirsiniz.</p>
    <p>Özellikle yabancı turistler için sunduğumuz bu <strong>şehirler arası transfer</strong> paketi, istenilen her an fotoğraf molası vermenizi sağlar. Kapadokya'ya ulaşımın lüks yolu olan <strong>şoförlü araç kiralama ankara</strong> hizmetimizle tatiliniz erken başlar.</p>
    """,
    "blog-ankara-bursa-vip-transfer": """
    <h2>Ankara Bursa Şoförlü VIP Transfer Hizmeti</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Tarih, doğa ve sanayinin kalbi Bursa'ya düzenleyeceğiniz iş veya gezi seyahatlerinde, <strong>şehirler arası vip transfer</strong> farkını hissetmelisiniz. Bu hatta en çok tercih edilen <strong>mercedes vito kiralama</strong> filomuz, ergonomik tasarımıyla uzun yola meydan okuyor.</p>
    <p>Hız, güvenlik ve prestij arayanlar için <strong>şehirler arası transfer</strong> departmanımız size özel rotalar çıkarır. Kapınıza kadar gelen <strong>şoförlü araç kiralama ankara</strong> ayrıcalığını yaşayın.</p>
    """,
    "blog-ankara-antalya-vip-transfer": """
    <h2>Ankara Antalya Lüks VIP Araçla Tatil Ulaşımı</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Yaz tatiliniz için Akdeniz'e giderken <strong>şehirler arası vip transfer</strong> hizmetimizle evinizden çıkıp otelinizin kapısına kadar süren kesintisiz bir lüks ulaşım sağlıyoruz.</p>
    <p>Aracın içindeki sistemleri ile Antalya'ya olan <strong>şehirler arası transfer</strong> süreci çocuklar için bile çok eğlenceli hale gelir. Özel tasarlanan <strong>şoförlü araç kiralama ankara</strong> paketimiz, tatilinize keyif katar.</p>
    """,
    "blog-ankara-izmir-vip-transfer": """
    <h2>Ankara İzmir Şoförlü Araç Kiralama ve VIP Transfer</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Ege'nin sıcak esintisine doğru yapacağınız seyahatlerde, <strong>şehirler arası vip transfer</strong> sistemimizle tanışın. Sınıfının en iyisi olan <strong>mercedes vito kiralama</strong> ile Ege yolculukları artık bambaşka bir boyutta.</p>
    <p>Gideceğiniz son noktaya kadar tek vasıtayla, valiz indirme bindirme stresi yaşamadan <strong>şehirler arası transfer</strong> kolaylığından yararlanın. Sağladığımız <strong>şoförlü araç kiralama ankara</strong> hizmetiyle İzmir seyahatleriniz çok daha hızlı ve elit.</p>
    """,
    "blog-sehirlerarasi-vip-transfer-fiyatlari": """
    <h2>2026 Şehirler Arası VIP Transfer Fiyatları</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Günümüzde lüks ulaşım sadece belirli bir kesimin değil, konforuna değer veren herkesin tercihi haline geldi. 2026 yılı <strong>şehirler arası vip transfer</strong> fiyatlarımız, <strong>mercedes vito kiralama</strong> ile kalabalık seyahatlerde kişi başı oldukça uygundur.</p>
    <p>Fiyat-performans açısından ideal olan <strong>şehirler arası transfer</strong> hizmetimizde, hiçbir gizli ödeme yoktur. Şeffaf fiyatlandırma politikamız ve kaliteli <strong>şoförlü araç kiralama ankara</strong> vizyonumuzla lideriz.</p>
    """,
    "blog-ankara-bodrum-vip-transfer": """
    <h2>Ankara Bodrum Kesintisiz Lüks VIP Ulaşım</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Bodrum'a giderken, özel tasarımlı araçlarımızla sunduğumuz <strong>şehirler arası vip transfer</strong> hizmeti, Bodrum yolunu sizin için adeta bir dinlenme molası yapar. Son model <strong>mercedes vito kiralama</strong> ile tatilinizin ilk gününe harika bir giriş yapabilirsiniz.</p>
    <p>İzole seyahat ihtiyacını, sunduğumuz <strong>şehirler arası transfer</strong> çözümleriyle en güvenli şekilde karşılıyoruz. Sunduğumuz <strong>şoförlü araç kiralama ankara</strong> hizmeti Bodrum sahillerine VIP giriş yapmanızı garantiliyor.</p>
    """,
    "blog-ankara-eskisehir-vip-transfer": """
    <h2>Ankara Eskişehir Günübirlik VIP Transfer</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Ankara'nın komşusu, kültür ve sanat şehri Eskişehir'e düzenleyeceğiniz geziler için <strong>şehirler arası vip transfer</strong> servisimiz emrinizdedir. Günübirlik turlarınızda sizi bekleyen <strong>mercedes vito kiralama</strong> araçlarımız size eşlik edebilir.</p>
    <p>Dönüş saatinize siz karar verin. Bu esnek <strong>şehirler arası transfer</strong> modeli, zaman yönetimini tamamen size bırakır. Şehre özel tahsis edilmiş <strong>şoförlü araç kiralama ankara</strong> hizmetimiz sayesinde Eskişehir yolculuklarınız pratik ve güvenli geçer.</p>
    """,
    "blog-ankara-konya-vip-transfer": """
    <h2>Ankara Konya Şoförlü VIP Araç Hizmeti</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Mevlana diyarı Konya'ya yapacağınız seyahatlerde <strong>şehirler arası vip transfer</strong> rahatlığına güvenin. Makam aracı konseptindeki sarsıntısız <strong>mercedes vito kiralama</strong> opsiyonlarımız sayesinde yol boyunca dinlenebilirsiniz.</p>
    <p>Aile büyükleri veya yabancı konuklarla yapılan seyahatlerde <strong>şehirler arası transfer</strong> büyük önem taşır. Sağladığımız <strong>şoförlü araç kiralama ankara</strong> hizmeti, Konya gezilerinize benzersiz bir prestij katar.</p>
    """,
    "blog-sehirlerarasi-soforlu-arac-kiralama": """
    <h2>Şehirler Arası Şoförlü Araç Kiralama Avantajları</h2>
    <p class="lead" style="font-size: 1.1rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">Uzun yolda yorulmak yerine <strong>şehirler arası vip transfer</strong> mantığını keşfetmelisiniz. Şoförlü araç kiralama, yolculuk boyunca sunulan bir asistans hizmetidir. İş amaçlı gezilerinizde <strong>mercedes vito kiralama</strong> ile yolda çalışabilirsiniz.</p>
    <p>Tüm <strong>şehirler arası transfer</strong> paketlerimiz operasyonel yükü omuzlarınızdan alır. Üst segment araçlarımızla gerçekleştirdiğimiz <strong>şoförlü araç kiralama ankara</strong> faaliyetlerimiz, size sadece yolculuğun keyfini çıkarma lüksünü sunar.</p>
    """
}

# Now rewrite each file correctly by replacing everything between <section class="blog-body"><div class="container"> and <div class="cta-box">
for slug, content_html in contents.items():
    filepath = os.path.join(cwd, f"{slug}.html")
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We need to replace the content inside the container
    body_pattern = r'(<section class="blog-body">\s*<div class="container">).*?(<div class="cta-box">)'
    replacement = f'\\1\n{content_html}\n\\2'
    
    new_html = re.sub(body_pattern, replacement, html, flags=re.DOTALL)
    
    # Ensure title inside h1 doesn't get messed up if needed, but the previous script already set h1 right.
    # The previous script replaced '<h1>.*?</h1>' to the new title. We can just verify it looks good.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"Actually updated content for {slug}.html")

print("Fixed the Regex and successfully updated all blogs with unique content!")
