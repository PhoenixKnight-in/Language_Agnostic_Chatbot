from typing import List
from model import FAQ
from database import db
import logging

logger = logging.getLogger(__name__)

class DataSeeder:
    @staticmethod
    async def seed_sample_faqs():
        """Seed database with sample FAQ data"""
        
        sample_faqs = [
            # Admissions
            {
                "question": "What are the admission requirements?",
                "answer": "Admission requirements vary by program. Generally, you need to have completed 12th grade with minimum 60% marks, pass our entrance exam, and submit required documents including academic transcripts, ID proof, and passport photos.",
                "keywords": ["admission", "requirements", "eligibility", "entrance", "12th", "marks"],
                "category": "admissions",
                "languages": {
                    "hi": {
                        "question": "प्रवेश की आवश्यकताएं क्या हैं?",
                        "answer": "प्रवेश की आवश्यकताएं कार्यक्रम के अनुसार अलग-अलग होती हैं। आमतौर पर, आपको न्यूनतम 60% अंकों के साथ 12वीं कक्षा पूरी करनी होगी, हमारी प्रवेश परीक्षा पास करनी होगी, और शैक्षणिक प्रतिलेख, पहचान प्रमाण, और पासपोर्ट फोटो सहित आवश्यक दस्तावेज जमा करने होंगे।"
                    },
                }
            },
            # Alumni & Networking
            {
                "question": "How active is the alumni network and what support do they provide?",
                "answer": "VIT has a strong alumni network of 2,00,000+ graduates globally working in top companies like Google, Microsoft, Apple, and leading startups. Alumni support includes: mentorship programs, industry connections, job referrals, guest lectures, funding for student projects, and networking events. Alumni chapters exist in 50+ cities worldwide.",
                "keywords": ["alumni", "network", "mentorship", "connections", "referrals", "global"],
                "category": "placement",
                "languages": {
                    "hi": {
                        "question": "पूर्व छात्र नेटवर्क कितना सक्रिय है और वे कौन सा समर्थन प्रदान करते हैं?",
                        "answer": "VIT के पास Google, Microsoft, Apple, और अग्रणी स्टार्टअप्स में काम करने वाले 2,00,000+ स्नातकों का एक मजबूत पूर्व छात्र नेटवर्क है। पूर्व छात्र समर्थन में शामिल है: मार्गदर्शन कार्यक्रम, उद्योग संपर्क, नौकरी रेफरल, अतिथि व्याख्यान, छात्र परियोजनाओं के लिए धन, और नेटवर्किंग इवेंट्स। दुनिया भर के 50+ शहरों में पूर्व छात्र चैप्टर्स मौजूद हैं।"
                    },
                    "ta": {
                        "question": "முன்னாள் மாணவர் நெட்வொர்க் எவ்வளவு சक்தியுடன் உள்ளது மற்றும் அவர்கள் என்ன ஆதரவு வழங்குகிறார்கள்?",
                        "answer": "VIT க்கு Google, Microsoft, Apple, மற்றும் முன்னணி தொடக்க நிறுவனங்களில் பணிபுரியும் 2,00,000+ பட்டதாரிகளின் வலுவான முன்னாள் மாணவர் நெட்வொர்க் உள்ளது. முன்னாள் மாணவர் ஆதரவில் அடங்கியவை: வழிகாட்டுதல் திட்டங்கள், தொழில்துறை தொடர்புகள், வேலை பரிந்துரைகள், விருந்தினர் விரிவுரைகள், மாணவர் திட்டங்களுக்கு நிதியுதவி, மற்றும் நெட்வொர்க்கிங் நிகழ்வுகள். உலகம் முழுவதும் 50+ நகரங்களில் முன்னாள் மாணவர் அத்தியாயங்கள் உள்ளன."
                    }
                }
            },
            
            # Examination System
            {
                "question": "What is the examination pattern and evaluation system?",
                "answer": "VIT follows continuous assessment with: CAT (Continuous Assessment Tests) - 30%, FAT (Final Assessment Test) - 70%, Assignment/Project work - additional 10-15%. There are 2 CATs and 1 FAT per semester. Online proctored exams available. Revaluation and supplementary exam provisions exist for eligible students.",
                "keywords": ["examination", "CAT", "FAT", "evaluation", "assessment", "revaluation"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "परीक्षा पैटर्न और मूल्यांकन प्रणाली क्या है?",
                        "answer": "VIT निरंतर मूल्यांकन का पालन करता है: CAT (निरंतर मूल्यांकन परीक्षा) - 30%, FAT (अंतिम मूल्यांकन परीक्षा) - 70%, असाइनमेंट/प्रोजेक्ट कार्य - अतिरिक्त 10-15%। प्रति सेमेस्टर 2 CAT और 1 FAT होते हैं। ऑनलाइन प्रोक्टर्ड परीक्षाएं उपलब्ध हैं। योग्य छात्रों के लिए पुनर्मूल्यांकन और पूरक परीक्षा प्रावधान मौजूद हैं।"
                    },
                    "ta": {
                        "question": "தேர்வு முறை மற்றும் மதிப்பீட்டு அமைப்பு என்ன?",
                        "answer": "VIT தொடர்ச்சியான மதிப்பீட்டைப் பின்பற்றுகிறது: CAT (தொடர்ச்சியான மதிப்பீட்டு தேர்வுகள்) - 30%, FAT (இறுதி மதிப்பீட்டு தேர்வு) - 70%,과제/திட்ட பணி - கூடுதல் 10-15%. ஒவ்வொரு செமஸ்டருக்கும் 2 CAT மற்றும் 1 FAT உள்ளது. ஆன்லைன் கண்காணிக்கப்பட்ட தேர்வுகள் கிடைக்கின்றன. தகுதியான மாணவர்களுக்கு மறு மதிப்பீடு மற்றும் கூடுதல் தேர்வு ஏற்பாடுகள் உள்ளன."
                    }
                }
            },
            
            # Sports & Recreation
            {
                "question": "What sports and recreational facilities are available?",
                "answer": "VIT offers extensive sports facilities: Olympic-size swimming pool, cricket grounds, basketball courts, tennis courts, badminton courts, football fields, volleyball courts, athletics track, gymnasium with modern equipment, indoor games (chess, carrom, table tennis), and dedicated sports coaching staff. Regular inter-collegiate tournaments held.",
                "keywords": ["sports", "recreation", "swimming", "cricket", "basketball", "gymnasium", "coaching"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कौन से खेल और मनोरंजन सुविधाएं उपलब्ध हैं?",
                        "answer": "VIT व्यापक खेल सुविधाएं प्रदान करता है: ओलंपिक-साइज़ स्विमिंग पूल, क्रिकेट मैदान, बास्केटबॉल कोर्ट, टेनिस कोर्ट, बैडमिंटन कोर्ट, फुटबॉल फील्ड, वॉलीबॉल कोर्ट, एथलेटिक्स ट्रैक, आधुनिक उपकरणों के साथ जिमनेसियम, इंडोर गेम्स (शतरंज, कैरम, टेबल टेनिस), और समर्पित खेल कोचिंग स्टाफ। नियमित अंतर-कॉलेजिएट टूर्नामेंट आयोजित किए जाते हैं।"
                    },
                    "ta": {
                        "question": "என்ன விளையாட்டு மற்றும் பொழுதுபோக்கு வசதிகள் உள்ளன?",
                        "answer": "VIT விரிவான விளையாட்டு வசதிகளை வழங்குகிறது: ஒலிம்பிக் அளவு நீச்சல் குளம், கிரிக்கெட் மைதானங்கள், கூடைப்பந்து மைதானங்கள், டென்னிஸ் மைதானங்கள், பேட்மின்டன் மைதானங்கள், கால்பந்து மைதானங்கள், கைப்பந்து மைதானங்கள், தடகள பாதை, நவீன உபகரணங்களுடன் கூடிய உடற்பயிற்சி கூடம், உள்ளரங்க விளையாட்டுகள் (சதுரங்கம், கேரம், டேபிள் டென்னிஸ்), மற்றும் பிரத்யேக விளையாட்டு பயிற்சி பணியாளர்கள். வழக்கமான கல்லூரிகளுக்கு இடையேயான போட்டிகள் நடத்தப்படுகின்றன."
                    }
                }
            },
            
            # Safety & Security
            {
                "question": "What safety and security measures are in place on campus?",
                "answer": "VIT ensures comprehensive safety: 24/7 security personnel, CCTV surveillance across campus, controlled access gates with ID cards, emergency helpline numbers, fire safety systems, night patrol services, separate security for hostels, anti-ragging measures, grievance redressal committee, and regular safety drills. Women's safety is given special priority.",
                "keywords": ["safety", "security", "CCTV", "emergency", "patrol", "anti-ragging", "women"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कैंपस में कौन से सुरक्षा और सुरक्षा उपाय हैं?",
                        "answer": "VIT व्यापक सुरक्षा सुनिश्चित करता है: 24/7 सुरक्षा कर्मचारी, पूरे कैंपस में CCTV निगरानी, ID कार्ड के साथ नियंत्रित पहुंच गेट, आपातकालीन हेल्पलाइन नंबर, अग्नि सुरक्षा प्रणालियां, रात्रि गश्ती सेवाएं, छात्रावासों के लिए अलग सुरक्षा, रैगिंग विरोधी उपाय, शिकायत निवारण समिति, और नियमित सुरक्षा ड्रिल। महिलाओं की सुरक्षा को विशेष प्राथमिकता दी जाती है।"
                    },
                    "ta": {
                        "question": "வளாகத்தில் என்ன பாதுகாப்பு மற்றும் பாதுகாப்பு நடவடிக்கைகள் உள்ளன?",
                        "answer": "VIT விரிவான பாதுகாப்பை உறுதி செய்கிறது: 24/7 பாதுகாப்பு பணியாளர்கள், வளாகம் முழுவதும் CCTV கண்காணிப்பு, ID கார்டுகளுடன் கட்டுப்படுத்தப்பட்ட அணுகல் வாயில்கள், அவசர உதவி எண்கள், தீ பாதுகாப்பு அமைப்புகள், இரவு ரோந்து சேவைகள், விடுதிகளுக்கு தனி பாதுகாப்பு, கொடுமைப்படுத்துதல் எதிர்ப்பு நடவடிக்கைகள், புகார் தீர்வு குழு, மற்றும் வழக்கமான பாதுகாப்பு பயிற்சிகள். பெண்களின் பாதுகாப்புக்கு சிறப்பு முன்னுரிமை அளிக்கப்படுகிறது."
                    }
                }
            },
            
            # Environmental Initiatives
            {
                "question": "What environmental sustainability initiatives does VIT have?",
                "answer": "VIT is committed to sustainability: Solar power generation (2 MW capacity), rainwater harvesting systems, waste segregation and recycling programs, green buildings with energy-efficient design, electric vehicle charging stations, organic waste composting, tree plantation drives, plastic-free campus initiatives, and environmental awareness programs.",
                "keywords": ["environment", "sustainability", "solar", "green", "recycling", "energy", "eco-friendly"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "VIT के पास कौन सी पर्यावरणीय स्थिरता पहल हैं?",
                        "answer": "VIT स्थिरता के लिए प्रतिबद्ध है: सौर ऊर्जा उत्पादन (2 MW क्षमता), वर्षा जल संचयन प्रणालियां, अपशिष्ट पृथक्करण और पुनर्चक्रण कार्यक्रम, ऊर्जा-कुशल डिजाइन के साथ हरित भवन, इलेक्ट्रिक वाहन चार्जिंग स्टेशन, जैविक अपशिष्ट कंपोस्टिंग, वृक्षारोपण अभियान, प्लास्टिक-मुक्त कैंपस पहल, और पर्यावरणीय जागरूकता कार्यक्रम।"
                    },
                    "ta": {
                        "question": "VIT க்கு என்ன சுற்றுச்சூழல் நிலைத்தன்மை முயற்சிகள் உள்ளன?",
                        "answer": "VIT நிலைத்தன்மைக்கு அர்ப்பணிக்கப்பட்டுள்ளது: சூரிய சக்தி உற்பத்தி (2 MW திறன்), மழைநீர் சேகரிப்பு அமைப்புகள், கழிவு பிரிப்பு மற்றும் மறுசுழற்சி திட்டங்கள், ऊर்ஜா திறன் வடிவமைப்புடன் பசுமை கட்டிடங்கள், மின்சார வாகன சார்ஜிங் நிலையங்கள், கரிம கழிவு உரமாக்குதல், மரம் நடுதல் இயக்கங்கள், பிளாஸ்டிக் இல்லா வளாக முயற்சிகள், மற்றும் சுற்றுச்சூழல் விழிப்புணர்வு திட்டங்கள்."
                    }
                }
            },
            # Fees
            {
                "question": "What are the tuition fees for different courses?",
                "answer": "Tuition fees vary by program: Engineering courses: ₹80,000-120,000 per year, Management courses: ₹60,000-90,000 per year, Arts/Science: ₹30,000-50,000 per year. Additional fees include laboratory, library, and examination fees.",
                "keywords": ["fees", "tuition", "cost", "payment", "courses", "engineering", "management"],
                "category": "fees",
                "languages": {
                    "hi": {
                        "question": "विभिन्न पाठ्यक्रमों के लिए ट्यूशन फीस क्या है?",
                        "answer": "ट्यूशन फीस कार्यक्रम के अनुसार अलग होती है: इंजीनियरिंग पाठ्यक्रम: ₹80,000-120,000 प्रति वर्ष, प्रबंधन पाठ्यक्रम: ₹60,000-90,000 प्रति वर्ष, कला/विज्ञान: ₹30,000-50,000 प्रति वर्ष। अतिरिक्त शुल्क में प्रयोगशाला, पुस्तकालय और परीक्षा शुल्क शामिल हैं।"
                    },
                    "ta": {
                        "question": "வெவ்வேறு படிப்புகளுக்கான கல்விக் கட்டணம் என்ன?",
                        "answer": "கல்விக் கட்டணம் திட்டத்தின் அடிப்படையில் மாறுபடும்: பொறியியல் படிப்புகள்: ஆண்டுக்கு ₹80,000-120,000, மேலாண்மை படிப்புகள்: ஆண்டுக்கு ₹60,000-90,000, கலை/அறிவியல்: ஆண்டுக்கு ₹30,000-50,000। கூடுதல் கட்டணங்களில் ஆய்வகம், நூலகம் மற்றும் தேர்வு கட்டணங்கள் அடங்கும்."
                    }
                }
            },
            
            # Academics
            {
                "question": "When will the semester results be declared?",
                "answer": "Semester results are typically declared within 4-6 weeks after the examination ends. Results are published on the college website and students are notified via SMS and email. You can check results using your roll number and date of birth.",
                "keywords": ["results", "semester", "exam", "declaration", "marks", "grades"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "सेमेस्टर परिणाम कब घोषित होंगे?",
                        "answer": "सेमेस्टर परिणाम आमतौर पर परीक्षा समाप्त होने के 4-6 सप्ताह के भीतर घोषित होते हैं। परिणाम कॉलेज की वेबसाइट पर प्रकाशित किए जाते हैं और छात्रों को SMS और ईमेल के माध्यम से सूचित किया जाता है। आप अपने रोल नंबर और जन्म तिथि का उपयोग करके परिणाम देख सकते हैं।"
                    },
                    "ta": {
                        "question": "செமஸ்டர் முடிவுகள் எப்போது அறிவிக்கப்படும்?",
                        "answer": "செமஸ்டர் முடிவுகள் பொதுவாக தேர்வு முடிந்த 4-6 வாரங்களுக்குள் அறிவிக்கப்படும். முடிவுகள் கல்லூரி இணையதளத்தில் வெளியிடப்பட்டு, மாணவர்களுக்கு SMS மற்றும் மின்னஞ்சل் மூலம் தெரிவிக்கப்படும். உங்கள் ரோல் எண் மற்றும் பிறந்த தேதியைப் பயன்படுத்தி முடிவுகளைச் சரிபார்க்கலாம்."
                    }
                }
            },
            
            # Schedule
            {
                "question": "What is the class timetable for this semester?",
                "answer": "Class timetables are available on the college website under the 'Academics' section. Timetables are also posted on department notice boards. Classes typically run from 9:00 AM to 4:30 PM with lunch break from 12:30 PM to 1:30 PM.",
                "keywords": ["timetable", "schedule", "classes", "timing", "semester"],
                "category": "schedule",
                "languages": {
                    "hi": {
                        "question": "इस सेमेस्टर के लिए कक्षा समय सारणी क्या है?",
                        "answer": "कक्षा समय सारणी कॉलेज की वेबसाइट पर 'शिक्षाविद्' खंड के तहत उपलब्ध है। समय सारणी विभाग के नोटिस बोर्ड पर भी पोस्ट की जाती है। कक्षाएं आमतौर पर सुबह 9:00 बजे से शाम 4:30 बजे तक चलती हैं और दोपहर 12:30 बजे से 1:30 बजे तक लंच ब्रेक होता है।"
                    },
                    "ta": {
                        "question": "இந்த செமஸ்டருக்கான வகுப்பு நேர அட்டவணை என்ন?",
                        "answer": "வகுப்பு நேர அட்டவணைகள் கல்லூரி இணையதளத்தில் 'கல்வி' பிரிவின் கீழ் கிடைக்கின்றன। நேர அட்டவணைகள் துறை அறிவிப்பு பலகைகளிலும் வெளியிடப்படுகின்றன। வகுப்புகள் பொதுவாக காலை 9:00 மணி முதல் மாலை 4:30 மணி வரை நடக்கும், மதிய உணவு இடைவேளை மதியம் 12:30 முதல் 1:30 வரை."
                    }
                }
            },
            
            # Facilities
            {
                "question": "What facilities are available in the college library?",
                "answer": "The library offers: 50,000+ books, digital resources, 100 reading seats, air conditioning, Wi-Fi, photocopying services, and computer terminals. Library hours: 8:00 AM to 8:00 PM (Monday-Saturday), 10:00 AM to 6:00 PM (Sunday).",
                "keywords": ["library", "facilities", "books", "reading", "hours", "services"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कॉलेज पुस्तकालय में कौन सी सुविधाएं उपलब्ध हैं?",
                        "answer": "पुस्तकालय में शामिल है: 50,000+ पुस्तकें, डिजिटल संसाधन, 100 पठन सीटें, एयर कंडीशनिंग, Wi-Fi, फोटोकॉपी सेवाएं, और कंप्यूटर टर्मिनल। पुस्तकालय के समय: सुबह 8:00 बजे से रात 8:00 बजे (सोमवार-शनिवार), सुबह 10:00 बजे से शाम 6:00 बजे (रविवार)।"
                    },
                    "ta": {
                        "question": "கல்லூரி நூலகத்தில் என்ன வசதிகள் உள்ளன?",
                        "answer": "நூலகத்தில் உள்ளவை: 50,000+ புத்தகங்கள், டிஜிட்டல் ஆதாரங்கள், 100 படிக்கும் இடங்கள், ஏர் கண்டிஷனிங், Wi-Fi, புகைப்பட நகல் சேவைகள், மற்றும் கணினி முனையங்கள். நூலக நேரம்: காலை 8:00 முதல் இரவு 8:00 வரை (திங்கள்-சனி), காலை 10:00 முதல் மாலை 6:00 வரை (ஞாயிறு)."
                    }
                }
            },
            
            # Scholarships
            {
                "question": "What scholarships are available for students?",
                "answer": "Available scholarships include: Merit-based scholarships (up to 50% tuition waiver), Need-based financial aid, Government scholarships for SC/ST/OBC students, Sports scholarships, and Special scholarships for outstanding academic performance. Application deadlines vary by scholarship type.",
                "keywords": ["scholarship", "financial", "aid", "merit", "government", "sports"],
                "category": "fees",
                "languages": {
                    "hi": {
                        "question": "छात्रों के लिए कौन सी छात्रवृत्तियां उपलब्ध हैं?",
                        "answer": "उपलब्ध छात्रवृत्तियों में शामिल हैं: मेधा-आधारित छात्रवृत्ति (50% तक ट्यूशन छूट), आवश्यकता-आधारित वित्तीय सहायता, SC/ST/OBC छात्रों के लिए सरकारी छात्रवृत्ति, खेल छात्रवृत्ति, और उत्कृष्ट शैक्षणिक प्रदर्शन के लिए विशेष छात्रवृत्ति। आवेदन की अंतिम तिथि छात्रवृत्ति के प्रकार के अनुसार अलग होती है।"
                    },
                    "ta": {
                        "question": "மாணவர்களுக்கு என்ன உதவித்தொகைகள் கிடைக்கின்றன?",
                        "answer": "கிடைக்கும் உதவித்தொகைகள்: தகுதி அடிப்படையிலான உதவித்தொகை (50% வரை கல்விக் கட்டண விலக்கு), தேவை அடிப்படையிலான நிதி உதவி, SC/ST/OBC மாணவர்களுக்கான அரசு உதவித்தொகை, விளையாட்டு உதவித்தொகை, மற்றும் சிறந்த கல்வி செயல்பாட்டிற்கான சிறப்பு உதவித்தொகை. விண்ணப்ப கடைசி தேதி உதவித்தொகை வகையைப் பொறுத்து மாறுபடும்."
                    }
                }
            },
            
            # Placement
            {
                "question": "How is the placement record of the college?",
                "answer": "Our placement record is excellent with 85% placement rate. Top recruiters include TCS, Infosys, Wipro, Accenture, and many startups. Average package is ₹4.5 LPA with highest package reaching ₹12 LPA. We have dedicated placement cell and conduct regular training programs.",
                "keywords": ["placement", "job", "recruitment", "companies", "package", "career"],
                "category": "placement",
                "languages": {
                    "hi": {
                        "question": "कॉलेज का प्लेसमेंट रिकॉर्ड कैसा है?",
                        "answer": "हमारा प्लेसमेंट रिकॉर्ड 85% प्लेसमेंट दर के साथ उत्कृष्ट है। शीर्ष रिक्रूटर्स में TCS, Infosys, Wipro, Accenture, और कई स्टार्टअप शामिल हैं। औसत पैकेज ₹4.5 LPA है और सर्वोच्च पैकेज ₹12 LPA तक पहुंचा है। हमारे पास समर्पित प्लेसमेंट सेल है और नियमित प्रशिक्षण कार्यक्रम आयोजित करते हैं।"
                    },
                    "ta": {
                        "question": "கல்லூரியின் வேலைவாய்ப்பு பதிவு எப்படி இருக்கிறது?",
                        "answer": "எங்கள் வேலைவாய்ப்பு பதிவு 85% வேலைவாய்ப்பு விகிதத்துடன் சிறந்தது। முக்கிய ஆட்சேர்ப்பாளர்களில் TCS, Infosys, Wipro, Accenture மற்றும் பல தொடக்க நிறுவனங்கள் அடங்கும். சராசரி பேக்கேஜ் ₹4.5 LPA ஆகும், மற்றும் அதிகபட்ச பேக்கேஜ் ₹12 LPA வரை சென்றுள்ளது. எங்களிடம் பிரத்யேக வேலைவாய்ப்பு பிரிவு உள்ளது மற்றும் வழக்கமான பயிற்சி திட்டங்களை நடத்துகிறோம்."
                    }
                }
            },
            
            # Admissions - Additional
            {
                "question": "Is there any entrance exam for admission?",
                "answer": "Yes, VIT conducts VITEEE (VIT Engineering Entrance Examination) for engineering courses. For other programs, we have separate entrance tests. The exam is computer-based and covers Physics, Chemistry, Mathematics, and English. Application for entrance exam opens in October.",
                "keywords": ["entrance", "exam", "VITEEE", "test", "application", "computer"],
                "category": "admissions",
                "languages": {
                    "hi": {
                        "question": "क्या प्रवेश के लिए कोई प्रवेश परीक्षा है?",
                        "answer": "हां, VIT इंजीनियरिंग पाठ्यक्रमों के लिए VITEEE (VIT इंजीनियरिंग प्रवेश परीक्षा) आयोजित करता है। अन्य कार्यक्रमों के लिए, हमारे पास अलग प्रवेश परीक्षाएं हैं। परीक्षा कंप्यूटर-आधारित है और इसमें भौतिकी, रसायन, गणित और अंग्रेजी शामिल हैं। प्रवेश परीक्षा के लिए आवेदन अक्टूबर में खुलता है।"
                    },
                    "ta": {
                        "question": "சேர்க்கைக்கு ஏதேனும் நுழைவுத் தேர்வு உள்ளதா?",
                        "answer": "ஆம், VIT பொறியியல் படிப்புகளுக்கு VITEEE (VIT பொறியியல் நுழைவுத் தேர்வு) நடத்துகிறது. மற்ற திட்டங்களுக்கு, எங்களுக்கு தனி நுழைவுத் தேர்வுகள் உள்ளன. தேர்வு கணினி அடிப்படையிலானது மற்றும் இயற்பியல், வேதியியல், கணிதம் மற்றும் ஆங்கிலம் ஆகியவற்றை உள்ளடக்கியது. நுழைவுத் தேர்வுக்கான விண்ணப்பம் அக்டோபரில் தொடங்குகிறது."
                    }
                }
            },
            
            {
                "question": "What documents are required for admission?",
                "answer": "Required documents: 10th and 12th mark sheets, Transfer Certificate, Conduct Certificate, Entrance exam scorecard, Passport size photos (8 copies), Aadhar card, Caste certificate (if applicable), Income certificate, and Migration certificate from previous institution.",
                "keywords": ["documents", "certificates", "marksheet", "transfer", "aadhar", "photos"],
                "category": "admissions",
                "languages": {
                    "hi": {
                        "question": "प्रवेश के लिए कौन से दस्तावेज आवश्यक हैं?",
                        "answer": "आवश्यक दस्तावेज: 10वीं और 12वीं की मार्कशीट, स्थानांतरण प्रमाणपत्र, आचरण प्रमाणपत्र, प्रवेश परीक्षा स्कोरकार्ड, पासपोर्ट साइज फोटो (8 प्रतियां), आधार कार्ड, जाति प्रमाणपत्र (यदि लागू हो), आय प्रमाणपत्र, और पिछली संस्था से स्थानांतरण प्रमाणपत्र।"
                    },
                    "ta": {
                        "question": "சேர்க்கைக்கு என்ன ஆவணங்கள் தேவை?",
                        "answer": "தேவையான ஆவணங்கள்: 10வது மற்றும் 12வது மதிப்பெண் பத்திரங்கள், இடமாற்றச் சான்றிதழ், நடத்தைச் சான்றிதழ், நுழைவுத் தேர்வு மதிப்பெண் அட்டை, பாஸ்போர்ட் அளவு புகைப்படங்கள் (8 பிரதிகள்), ஆதார் அட்டை, சாதிச் சான்றிதழ் (பொருந்தினால்), வருமானச் சான்றிதழ், மற்றும் முந்தைய நிறுவனத்திலிருந்து இடமாற்றச் சான்றிதழ்."
                    }
                }
            },
            
            # Academics - Additional
            {
                "question": "What is the grading system used in the university?",
                "answer": "VIT follows a 10-point GPA system. Grade A+ (90-100) = 10 points, A (80-89) = 9 points, B+ (70-79) = 8 points, B (60-69) = 7 points, C+ (55-59) = 6 points, C (50-54) = 5 points, D (45-49) = 4 points, F (Below 45) = 0 points. CGPA is calculated based on credit-weighted average.",
                "keywords": ["grading", "GPA", "CGPA", "marks", "points", "system"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "विश्वविद्यालय में कौन सी ग्रेडिंग प्रणाली का उपयोग किया जाता है?",
                        "answer": "VIT 10-पॉइंट GPA सिस्टम का पालन करता है। ग्रेड A+ (90-100) = 10 पॉइंट, A (80-89) = 9 पॉइंट, B+ (70-79) = 8 पॉइंट, B (60-69) = 7 पॉइंट, C+ (55-59) = 6 पॉइंट, C (50-54) = 5 पॉइंट, D (45-49) = 4 पॉइंट, F (45 से नीचे) = 0 पॉइंट। CGPA क्रेडिट-भारित औसत के आधार पर गणना की जाती है।"
                    },
                    "ta": {
                        "question": "பல்கலைக்கழகத்தில் என்ன தரமிடும் முறை பயன்படுத்தப்படுகிறது?",
                        "answer": "VIT 10-புள்ளி GPA முறையைப் பின்பற்றுகிறது। தரம் A+ (90-100) = 10 புள்ளிகள், A (80-89) = 9 புள்ளிகள், B+ (70-79) = 8 புள்ளிகள், B (60-69) = 7 புள்ளிகள், C+ (55-59) = 6 புள்ளிகள், C (50-54) = 5 புள்ளிகள், D (45-49) = 4 புள்ளிகள், F (45க்கு கீழ்) = 0 புள்ளிகள். CGPA கிரெடிட்-எடையிடப்பட்ட சராசரியின் அடிப்படையில் கணக்கிடப்படுகிறது."
                    }
                }
            },
            
            {
                "question": "How many credits are required for graduation?",
                "answer": "Credit requirements vary by program: B.Tech requires 164-176 credits over 4 years, M.Tech requires 64 credits over 2 years, MBA requires 72 credits over 2 years, and Bachelor's programs in Arts/Science require 120-132 credits over 3-4 years. Students must maintain minimum 5.0 CGPA.",
                "keywords": ["credits", "graduation", "requirements", "btech", "mtech", "mba", "CGPA"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "स्नातक के लिए कितने क्रेडिट आवश्यक हैं?",
                        "answer": "क्रेडिट आवश्यकताएं कार्यक्रम के अनुसार अलग होती हैं: B.Tech के लिए 4 वर्षों में 164-176 क्रेडिट, M.Tech के लिए 2 वर्षों में 64 क्रेडिट, MBA के लिए 2 वर्षों में 72 क्रेडिट, और कला/विज्ञान में स्नातक कार्यक्रमों के लिए 3-4 वर्षों में 120-132 क्रेडिट आवश्यक हैं। छात्रों को न्यूनतम 5.0 CGPA बनाए रखना चाहिए।"
                    },
                    "ta": {
                        "question": "பட்டப்படிப்புக்கு எத்தனை கிரெடிட்கள் தேவை?",
                        "answer": "கிரெடிட் தேவைகள் திட்டத்தின் அடிப்படையில் மாறுபடும்: B.Tech க்கு 4 ஆண்டுகளில் 164-176 கிரெடிட்கள், M.Tech க்கு 2 ஆண்டுகளில் 64 கிரெடிட்கள், MBA க்கு 2 ஆண்டுகளில் 72 கிரெடிட்கள், மற்றும் கலை/அறிவியல் இளங்கலை திட்டங்களுக்கு 3-4 ஆண்டுகளில் 120-132 கிரெடிட்கள் தேவை. மாணவர்கள் குறைந்தம் 5.0 CGPA பராமரிக்க வேண்டும்."
                    }
                }
            },
            
            {
                "question": "Can I change my branch/specialization after admission?",
                "answer": "Branch change is possible after first year based on academic performance and availability of seats. Students need minimum 8.5 CGPA in first year and should apply during the specified window in May-June. Branch change is subject to fulfillment of eligibility criteria and merit list.",
                "keywords": ["branch", "change", "specialization", "CGPA", "merit", "eligibility"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "क्या मैं प्रवेश के बाद अपनी शाखा/विशेषज्ञता बदल सकता हूं?",
                        "answer": "शैक्षणिक प्रदर्शन और सीटों की उपलब्धता के आधार पर पहले वर्ष के बाद शाखा परिवर्तन संभव है। छात्रों को पहले वर्ष में न्यूनतम 8.5 CGPA चाहिए और मई-जून में निर्दिष्ट अवधि के दौरान आवेदन करना चाहिए। शाखा परिवर्तन पात्रता मानदंडों की पूर्ति और मेरिट सूची के अधीन है।"
                    },
                    "ta": {
                        "question": "சேர்க்கைக்குப் பிறகு எனது பிரிவு/நிபுணத்துவத்தை மாற்ற முடியுமா?",
                        "answer": "கல்வி செயல்பாடு மற்றும் இடங்கள் கிடைக்கும் தன்மையின் அடிப்படையில் முதல் ஆண்டுக்குப் பிறகு பிரிவு மாற்றம் சாத்தியம். மாணவர்களுக்கு முதல் ஆண்டில் குறைந்தம் 8.5 CGPA தேவை மற்றும் மே-ஜூன் மாதங்களில் குறிப்பிட்ட காலக்கெடுவில் விண்ணப்பிக்க வேண்டும். பிரிவு மாற்றம் தகுதி அளவுகோல்கள் மற்றும் தகுதி பட்டியலின் பூர்த்திக்கு உட்பட்டது."
                    }
                }
            },
            
            # Campus Life
            {
                "question": "What hostel facilities are available?",
                "answer": "VIT provides separate hostels for boys and girls with AC and non-AC rooms. Facilities include mess, Wi-Fi, laundry, recreational areas, gym, medical room, and 24/7 security. Room types: Single occupancy (₹80,000/year), Double sharing (₹60,000/year), Triple sharing (₹45,000/year). Hostel admission is based on distance from home.",
                "keywords": ["hostel", "accommodation", "mess", "wifi", "security", "rooms"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कौन सी छात्रावास सुविधाएं उपलब्ध हैं?",
                        "answer": "VIT लड़कों और लड़कियों के लिए AC और non-AC कमरों के साथ अलग छात्रावास प्रदान करता है। सुविधाओं में मेस, Wi-Fi, लॉन्ड्री, मनोरंजक क्षेत्र, जिम, मेडिकल रूम, और 24/7 सुरक्षा शामिल है। कमरे के प्रकार: एकल कब्जा (₹80,000/वर्ष), दोहरा साझाकरण (₹60,000/वर्ष), तिहरा साझाकरण (₹45,000/वर्ष)। छात्रावास प्रवेश घर से दूरी के आधार पर होता है।"
                    },
                    "ta": {
                        "question": "என்ன விடுதி வசதிகள் உள்ளன?",
                        "answer": "VIT ஆண் மற்றும் பெண் மாணவர்களுக்கு AC மற்றும் non-AC அறைகளுடன் தனித்தனி விடுதிகளை வழங்குகிறது. வசதிகளில் மெஸ், Wi-Fi, சலவை, பொழுதுபோக்கு பகுதிகள், உடற்பயிற்சி கூடம், மருத்துவ அறை மற்றும் 24/7 பாதுகாப்பு அடங்கும். அறை வகைகள்: ஒற்றை ஆக்கிரமிப்பு (₹80,000/ஆண்டு), இரட்டை பகிர்வு (₹60,000/ஆண்டு), மூன்று பகிர்வு (₹45,000/ஆண்டு)। விடுதி சேர்க்கை வீட்டிலிருந்து உள்ள தூரத்தின் அடிப்படையில் அமைகிறது."
                    }
                }
            },
            
            {
                "question": "What extracurricular activities are available?",
                "answer": "VIT offers diverse activities: 50+ student clubs, technical societies (IEEE, ACM, SAE), cultural clubs (drama, music, dance), sports teams, debate society, photography club, social service groups, entrepreneurship cell, and annual fest 'Riviera'. Students can join multiple clubs based on interests.",
                "keywords": ["clubs", "activities", "sports", "cultural", "technical", "fest", "societies"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कौन सी पाठ्येतर गतिविधियां उपलब्ध हैं?",
                        "answer": "VIT विविध गतिविधियां प्रदान करता है: 50+ छात्र क्लब, तकनीकी समितियां (IEEE, ACM, SAE), सांस्कृतिक क्लब (नाटक, संगीत, नृत्य), खेल टीमें, बहस समाज, फोटोग्राफी क्लब, सामाजिक सेवा समूह, उद्यमिता सेल, और वार्षिक उत्सव 'रिवेरा'। छात्र रुचि के आधार पर कई क्लबों में शामिल हो सकते हैं।"
                    },
                    "ta": {
                        "question": "என்ன பாடेतर நடவடிக்கைகள் கிடைக்கின்றன?",
                        "answer": "VIT பல்வேறு நடவடிக்கைகளை வழங்குகிறது: 50+ மாணவர் குழுக்கள், தொழில்நுட்ப சங்கங்கள் (IEEE, ACM, SAE), கலாச்சார குழுக்கள் (நாடகம், இசை, நடனம்), விளையாட்டு அணிகள், விவாத சங்கம், புகைப்படக் குழு, சமூக சேவை குழுக்கள், தொழில்முனைவோர் பிரிவு, மற்றும் வருடாந்த விழா 'ரிவேரா'. மாணவர்கள் ஆர்வத்தின் அடிப்படையில் பல குழுக்களில் சேரலாம்."
                    }
                }
            },
            {
                "question": "Tell me about the campus life?",
                "answer": "VIT campus life is vibrant and well-structured: Daily routine starts at 6:00 AM with morning activities, classes from 8:00 AM to 5:00 PM with breaks, evening time for sports/clubs/studies from 5:00 PM to 8:00 PM. Campus has 24/7 Wi-Fi, multiple food courts, cafeterias, and recreational areas. Students engage in technical clubs, cultural activities, sports, and social events. Strict but supportive environment with mentor-mentee system, regular counseling, and academic support.",
                "keywords": ["campus", "life", "daily", "routine", "activities", "students", "environment"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "VIT कैंपस में रहने वाले छात्रों का दैनिक जीवन कैसा होता है?",
                        "answer": "VIT कैंपस जीवन जीवंत और सुव्यवस्थित है: दैनिक दिनचर्या सुबह 6:00 बजे सुबह की गतिविधियों के साथ शुरू होती है, सुबह 8:00 बजे से शाम 5:00 बजे तक ब्रेक के साथ कक्षाएं, शाम 5:00 बजे से रात 8:00 बजे तक खेल/क्लब/अध्ययन का समय। कैंपस में 24/7 Wi-Fi, कई फूड कोर्ट, कैफेटेरिया और मनोरंजक क्षेत्र हैं। छात्र तकनीकी क्लब, सांस्कृतिक गतिविधियों, खेल और सामाजिक कार्यक्रमों में भाग लेते हैं। मेंटर-मेंटी सिस्टम, नियमित परामर्श और शैक्षणिक सहायता के साथ सख्त लेकिन सहायक वातावरण।"
                    },
                    "ta": {
                        "question": "VIT வளாகத்தில் வசிக்கும் மாணவர்களின் தினசரி வாழ்க்கை எப்படி இருக்கும்?",
                        "answer": "VIT வளாக வாழ்க்கை துடிப்பான மற்றும் நன்கு கட்டமைக்கப்பட்டது: தினசரி வழக்கம் காலை 6:00 மணிக்கு காலை நடவடிக்கைகளுடன் தொடங்குகிறது, காலை 8:00 முதல் மாலை 5:00 வரை இடைவேளையுடன் வகுப்புகள், மாலை 5:00 முதல் இரவு 8:00 வரை விளையாட்டு/குழுக்கள்/படிப்புக்கான நேரம். வளாகத்தில் 24/7 Wi-Fi, பல உணவு நீதிமன்றங்கள், உணவகங்கள் மற்றும் பொழுதுபோக்கு பகுதிகள் உள்ளன. மாணவர்கள் தொழில்நுட்ப குழுக்கள், கலாச்சார நடவடிக்கைகள், விளையாட்டு மற்றும் சமூக நிகழ்வுகளில் ஈடுபடுகின்றனர். வழிகாட்டி-மாணவர் அமைப்பு, வழக்கமான ஆலோசனை மற்றும் கல்வி ஆதரவுடன் கண்டிப்பான ஆனால் ஆதரவான சூழல்."
                    }
                }
            },

            {
                "question": "What cultural events and festivals are celebrated on campus?",
                "answer": "VIT celebrates diverse cultural events throughout the year: Annual cultural fest 'Riviera' (February) - South India's largest college fest with celebrity performances, competitions, and workshops. Religious festivals: Diwali, Holi, Eid, Christmas, Onam, Pongal with special celebrations and food. Regional celebrations: Bengali New Year, Gujarati festivals, etc. Technical fests, sports meets, freshers' welcome, farewell parties. International events celebrating diversity with students from 60+ countries.",
                "keywords": ["cultural", "events", "festivals", "riviera", "celebrations", "diversity", "international"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कैंपस में कौन से सांस्कृतिक कार्यक्रम और त्योहार मनाए जाते हैं?",
                        "answer": "VIT साल भर विविध सांस्कृतिक कार्यक्रम मनाता है: वार्षिक सांस्कृतिक उत्सव 'रिवेरा' (फरवरी) - सेलिब्रिटी प्रदर्शन, प्रतियोगिताओं और कार्यशालाओं के साथ दक्षिण भारत का सबसे बड़ा कॉलेज फेस्ट। धार्मिक त्योहार: दिवाली, होली, ईद, क्रिसमस, ओणम, पोंगल विशेष समारोह और भोजन के साथ। क्षेत्रीय समारोह: बंगाली नव वर्ष, गुजराती त्योहार, आदि। तकनीकी उत्सव, खेल मेले, नवागंतुकों का स्वागत, विदाई पार्टियां। 60+ देशों के छात्रों के साथ विविधता मनाने वाले अंतर्राष्ट्रीय कार्यक्रम।"
                    },
                    "ta": {
                        "question": "வளாகத்தில் என்ன கலாச்சார நிகழ்வுகள் மற்றும் பண்டிகைகள் கொண்டாடப்படுகின்றன?",
                        "answer": "VIT ஆண்டு முழுவதும் பல்வேறு கலாச்சார நிகழ்வுகளை கொண்டாடுகிறது: வருடாந்திர கலாச்சார விழா 'ரிவேரா' (பிப்ரவரி) - பிரபல நடிகர்களின் நிகழ்ச்சிகள், போட்டிகள் மற்றும் பட்டறைகளுடன் தென்னிந்தியாவின் மிகப்பெரிய கல்லூரி விழா. மத பண்டிகைகள்: தீபாவளி, ஹோலி, ஈது, கிறிஸ்மஸ், ஓணம், பொங்கல் சிறப்பு கொண்டாட்டங்கள் மற்றும் உணவுடன். பிராந்திய கொண்டாட்டங்கள்: பெங்காலி புத்தாண்டு, குஜராத்தி பண்டிகைகள், போன்றவை. தொழில்நுட்ப விழாக்கள், விளையாட்டு போட்டிகள், புதியவர்கள் வரவேற்பு, பிரியாவிடை விழாக்கள். 60+ நாடுகளில் இருந்து வந்த மாணவர்களுடன் பன்முகத்தன்மையை கொண்டாடும் சர்வதேச நிகழ்வுகள்."
                    }
                }
            },

            {
                "question": "What dining and food options are available on campus?",
                "answer": "VIT offers diverse dining options: 15+ food courts and cafeterias across campus serving North Indian, South Indian, Chinese, Continental, and fast food. Popular spots: Amul parlor, Subway, Dominos, Pizza Hut, local vendors. Hostel mess serves 4 meals daily with vegetarian/non-vegetarian options. Night canteens open till 2:00 AM. Food trucks, juice bars, and snack counters. Special arrangements during festivals. Affordable pricing: Meals from ₹40-200, mess monthly charges ₹4,500-5,200.",
                "keywords": ["dining", "food", "cafeteria", "mess", "restaurants", "canteen", "meals"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कैंपस में कौन से भोजन और खाद्य विकल्प उपलब्ध हैं?",
                        "answer": "VIT विविध भोजन विकल्प प्रदान करता है: कैंपस में 15+ फूड कोर्ट और कैफेटेरिया उत्तर भारतीय, दक्षिण भारतीय, चाइनीज, कॉन्टिनेंटल और फास्ट फूड परोसते हैं। लोकप्रिय स्थान: अमूल पार्लर, सबवे, डोमिनोज, पिज्जा हट, स्थानीय विक्रेता। होस्टल मेस शाकाहारी/मांसाहारी विकल्पों के साथ दैनिक 4 भोजन परोसता है। रात्रि कैंटीन सुबह 2:00 बजे तक खुली रहती है। फूड ट्रक, जूस बार, और स्नैक काउंटर। त्योहारों के दौरान विशेष व्यवस्था। किफायती मूल्य: भोजन ₹40-200, मेस मासिक शुल्क ₹4,500-5,200।"
                    },
                    "ta": {
                        "question": "வளாகத்தில் என்ன உணவு மற்றும் உணவு விருப்பங்கள் கிடைக்கின்றன?",
                        "answer": "VIT பல்வேறு உணவு விருப்பங்களை வழங்குகிறது: வளாகம் முழுவதும் 15+ உணவு நீதிமன்றங்கள் மற்றும் உணவகங்கள் வட இந்திய, தென் இந்திய, சீன, கான்டினென்டல் மற்றும் துரித உணவு வகைகளை வழங்குகின்றன. பிரபலமான இடங்கள்: அமுல் பார்லர், சப்வே, டோமினோஸ், பிட்சா ஹட், உள்ளூர் விற்பனையாளர்கள். விடுதி உணவகம் சைவ/அசைவ விருப்பங்களுடன் தினசரி 4 வேளை உணவு வழங்குகிறது. இரவு உணவகங்கள் அதிகாலை 2:00 மணி வரை திறந்திருக்கும். உணவு டிரக்குகள், பழச்சாறு பார்கள் மற்றும் தின்பண்ட கவுண்டர்கள். பண்டிகைகளின் போது சிறப்பு ஏற்பாடுகள். கட்டுப்படியாகும் விலை: உணவுகள் ₹40-200, உணவக மாதாந்திர கட்டணம் ₹4,500-5,200."
                    }
                }
            },

            {
                "question": "What recreational activities and entertainment options are available?",
                "answer": "VIT provides abundant recreational facilities: Indoor gaming zones with PS5, Xbox, PC gaming, pool tables, foosball. Movie screening halls showing latest films. Music and dance practice rooms with instruments. Art and craft workshops. Adventure sports: rock climbing wall, cycling tracks. Regular DJ nights, cultural performances, comedy shows. Shopping complex with clothing, electronics, stationery. Meditation and yoga centers. Reading lounges and quiet spaces for relaxation.",
                "keywords": ["recreation", "entertainment", "gaming", "movies", "music", "adventure", "shopping", "relaxation"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कौन सी मनोरंजक गतिविधियां और मनोरंजन के विकल्प उपलब्ध हैं?",
                        "answer": "VIT प्रचुर मात्रा में मनोरंजक सुविधाएं प्रदान करता है: PS5, Xbox, PC गेमिंग, पूल टेबल, फ़ूज़बॉल के साथ इंडोर गेमिंग ज़ोन। नवीनतम फिल्में दिखाने वाले मूवी स्क्रीनिंग हॉल। वाद्य यंत्रों के साथ संगीत और नृत्य अभ्यास कक्ष। कला और शिल्प कार्यशालाएं। साहसिक खेल: रॉक क्लाइंबिंग वॉल, साइकिलिंग ट्रैक। नियमित DJ नाइट्स, सांस्कृतिक प्रदर्शन, कॉमेडी शो। कपड़े, इलेक्ट्रॉनिक्स, स्टेशनरी के साथ शॉपिंग कॉम्प्लेक्स। ध्यान और योग केंद्र। आराम के लिए रीडिंग लाउंज और शांत स्थान।"
                    },
                    "ta": {
                        "question": "என்ன பொழுதுபோக்கு நடவடிக்கைகள் மற்றும் பொழுதுபோக்கு விருப்பங்கள் கிடைக்கின்றன?",
                        "answer": "VIT ஏராளமான பொழுதுபோக்கு வசதிகளை வழங்குகிறது: PS5, Xbox, PC கேமிங், பூல் டேபிள்கள், ஃபூஸ்பால் உடன் உள்ளரங்க விளையாட்டு மண்டலங்கள். சமீபத்திய திரைப்படங்களைக் காட்டும் திரைப்பட திரையிடல் அரங்குகள். இசைக்கருவிகளுடன் இசை மற்றும் நடன பயிற்சி அறைகள். கலை மற்றும் கைவினைப் பட்டறைகள். சாகசப் விளையாட்டுகள்: பாறை ஏறும் சுவர், சைக்கிள் ஓட்டும் பாதைகள். வழக்கமான DJ இரவுகள், கலாச்சார நிகழ்ச்சிகள், நகைச்சுவை நிகழ்ச்சிகள். ஆடை, எலக்ட்ரானிக்ஸ், எழுதுபொருட்களுடன் ஷாப்பிங் வளாகம். தியானம் மற்றும் யோகா மையங்கள். ஓய்வுக்கான வாசிப்பு அறைகள் மற்றும் அமைதியான இடங்கள்."
                    }
                }
            },

            {
                "question": "How is the social life and student community at VIT?",
                "answer": "VIT has a vibrant and diverse social community: Students from all Indian states and 60+ countries creating multicultural environment. 50+ active student clubs and societies for every interest. Strong senior-junior mentoring culture. Regular social events: freshers' parties, farewell celebrations, birthday celebrations in hostels. Diverse friendship groups across different cultures and backgrounds. Active social media communities and WhatsApp groups. Collaborative study groups and project teams. Supportive peer network for academics and personal growth.",
                "keywords": ["social", "community", "friends", "diversity", "multicultural", "clubs", "networking"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "VIT में सामाजिक जीवन और छात्र समुदाय कैसा है?",
                        "answer": "VIT में एक जीवंत और विविध सामाजिक समुदाय है: सभी भारतीय राज्यों और 60+ देशों के छात्र बहुसांस्कृतिक वातावरण बनाते हैं। हर रुचि के लिए 50+ सक्रिय छात्र क्लब और समितियां। मजबूत सीनियर-जूनियर मेंटरिंग संस्कृति। नियमित सामाजिक कार्यक्रम: नवागंतुक पार्टियां, विदाई समारोह, होस्टल में जन्मदिन समारोह। विभिन्न संस्कृतियों और पृष्ठभूमि के विविध दोस्ती समूह। सक्रिय सोशल मीडिया समुदाय और व्हाट्सएप ग्रुप्स। सहयोगी अध्ययन समूह और प्रोजेक्ट टीमें। शिक्षाविद् और व्यक्तिगत विकास के लिए सहायक सहकर्मी नेटवर्क।"
                    },
                    "ta": {
                        "question": "VIT யில் சமூக வாழ்க்கை மற்றும் மாணவர் சமூகம் எப்படி இருக்கிறது?",
                        "answer": "VIT யில் துடிப்பான மற்றும் பன்முக சமூக சமூகம் உள்ளது: அனைத்து இந்திய மாநிலங்கள் மற்றும் 60+ நாடுகளின் மாணவர்கள் பல்கலாச்சார சூழலை உருவாக்குகின்றனர். ஒவ்வொரு ஆர்வத்திற்கும் 50+ செயலில் உள்ள மாணவர் குழுக்கள் மற்றும் சங்கங்கள். வலுவான மூத்த-இளைய வழிகாட்டுதல் கலாச்சாரம். வழக்கமான சமூக நிகழ்வுகள்: புதியவர்கள் பார்ட்டிகள், பிரியாவிடை கொண்டாட்டங்கள், விடுதிகளில் பிறந்தநாள் கொண்டாட்டங்கள். வெவ்வேறு கலாச்சாரங்கள் மற்றும் பின்னணிகளில் பல்வேறு நட்பு குழுக்கள். செயலில் உள்ள சமூக ஊடக சமூகங்கள் மற்றும் WhatsApp குழுக்கள். ஒத்துழைப்பு படிப்பு குழுக்கள் மற்றும் திட்டக் குழுக்கள். கல்வி மற்றும் தனிப்பட்ட வளர்ச்சிக்கான ஆதரவான சக நெட்வொர்க்."
                    }
                }
            },
            
            # Transportation
            {
                "question": "What transportation facilities are provided by the college?",
                "answer": "VIT provides comprehensive bus service covering major areas of Vellore and Chennai with 100+ buses. Bus routes cover residential areas, railway stations, and shopping centers. Monthly bus pass costs ₹1,200-2,500 depending on distance. College also provides shuttle service between campus and nearby areas during exam periods.",
                "keywords": ["bus", "transport", "routes", "pass", "shuttle", "campus"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कॉलेज द्वारा कौन सी परिवहन सुविधाएं प्रदान की जाती हैं?",
                        "answer": "VIT 100+ बसों के साथ वेल्लोर और चेन्नई के प्रमुख क्षेत्रों को कवर करने वाली व्यापक बस सेवा प्रदान करता है। बस रूट्स आवासीय क्षेत्रों, रेलवे स्टेशनों और शॉपिंग सेंटरों को कवर करते हैं। मासिक बस पास की लागत दूरी के आधार पर ₹1,200-2,500 है। कॉलेज परीक्षा अवधि के दौरान कैंपस और आसपास के क्षेत्रों के बीच शटल सेवा भी प्रदान करता है।"
                    },
                    "ta": {
                        "question": "கல்லூரியால் என்ன போக்குவரத்து வசதிகள் வழங்கப்படுகின்றன?",
                        "answer": "VIT 100+ பேருந்துகளுடன் வேலூர் மற்றும் சென்னையின் முக்கிய பகுதிகளை உள்ளடக்கிய விரிவான பேருந்து சேவையை வழங்குகிறது. பேருந்து வழித்தடங்கள் குடியிருப்பு பகுதிகள், இரயில் நிலையங்கள் மற்றும் வணிக மையங்களை உள்ளடக்குகிறது. மாதாந்திர பேருந்து பாஸ் தூரத்தைப் பொறுத்து ₹1,200-2,500 செலவாகும். கல்லூரி தேர்வு காலங்களில் வளாகம் மற்றும் அருகிலுள்ள பகுதிகளுக்கு இடையே ஷட்டில் சேவையும் வழங்குகிறது."
                    }
                }
            },
            
            # Research & Innovation
            {
                "question": "What research opportunities are available for students?",
                "answer": "VIT encourages student research through: Research internships with faculty, Summer Research Fellowship Program (SRFP), participation in sponsored projects, publication opportunities in journals/conferences, collaboration with industry partners, access to advanced labs and equipment, and funding support for innovative projects up to ₹50,000.",
                "keywords": ["research", "internships", "projects", "publications", "funding", "innovation"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "छात्रों के लिए कौन से अनुसंधान अवसर उपलब्ध हैं?",
                        "answer": "VIT छात्र अनुसंधान को प्रोत्साहित करता है: संकाय के साथ अनुसंधान इंटर्नशिप, ग्रीष्मकालीन अनुसंधान फेलोशिप कार्यक्रम (SRFP), प्रायोजित परियोजनाओं में भागीदारी, पत्रिकाओं/सम्मेलनों में प्रकाशन अवसर, उद्योग भागीदारों के साथ सहयोग, उन्नत प्रयोगशालाओं और उपकरणों तक पहुंच, और ₹50,000 तक की नवाचार परियोजनाओं के लिए धन सहायता।"
                    },
                    "ta": {
                        "question": "மாணவர்களுக்கு என்ன ஆராய்ச்சி வாய்ப்புகள் உள்ளன?",
                        "answer": "VIT மாணவர் ஆராய்ச்சியை ஊக்குவிக்கிறது: ஆசிரியர்களுடன் ஆராய்ச்சி பயிற்சி, கோடைகால ஆராய்ச்சி பெல்லோஷிப் திட்டம் (SRFP), நிதியுதவி பெற்ற திட்டங்களில் பங்கேற்பு, பத்திரிகைகள்/மாநாட்டுகளில் வெளியீட்டு வாய்ப்புகள், தொழில்துறை கூட்டாளர்களுடன் ஒத்துழைப்பு, மேம்பட்ட ஆய்வகங்கள் மற்றும் உபகரणங்களுக்கான அணுகல், மற்றும் ₹50,000 வரை புதுமையான திட்டங்களுக்கான நிதி உதவி."
                    }
                }
            },
            
            # International Programs
            {
                "question": "Does VIT offer international exchange programs?",
                "answer": "Yes, VIT has partnerships with 300+ universities worldwide for student exchange programs. Programs include semester abroad, summer schools, research collaborations, and dual degree programs. Popular destinations: USA, Germany, Australia, Singapore, UK. Students can apply in 3rd/4th year with minimum 7.5 CGPA. Financial assistance available.",
                "keywords": ["international", "exchange", "abroad", "partnerships", "dual", "degree"],
                "category": "academics",
                "languages": {
                    "hi": {
                        "question": "क्या VIT अंतर्राष्ट्रीय विनिमय कार्यक्रम प्रदान करता है?",
                        "answer": "हां, VIT के पास छात्र विनिमय कार्यक्रमों के लिए दुनिया भर की 300+ विश्वविद्यालयों के साथ साझेदारी है। कार्यक्रमों में विदेश में सेमेस्टर, ग्रीष्मकालीन स्कूल, अनुसंधान सहयोग, और दोहरी डिग्री कार्यक्रम शामिल हैं। लोकप्रिय गंतव्य: USA, जर्मनी, ऑस्ट्रेलिया, सिंगापुर, UK। छात्र न्यूनतम 7.5 CGPA के साथ 3rd/4th वर्ष में आवेदन कर सकते हैं। वित्तीय सहायता उपलब्ध है।"
                    },
                    "ta": {
                        "question": "VIT சர்வதேச மாற்று திட்டங்களை வழங்குகிறதா?",
                        "answer": "ஆம், VIT க்கு மாணவர் மாற்று திட்டங்களுக்காக உலகம் முழுவதும் 300+ பல்கலைக்கழகங்களுடன் கூட்டாண்மை உள்ளது. திட்டங்களில் வெளிநாட்டு செமஸ்டர், கோடைகால பள்ளிகள், ஆராய்ச்சி ஒத்துழைப்புகள் மற்றும் இரட்டை பட்டம் திட்டங்கள் அடங்கும். பிரபலமான இடங்கள்: அமெரிக்கா, ஜெர்மனி, ஆஸ்திரேலியா, சிங்கப்பூர், இங்கிலாந்து. மாணவர்கள் குறைந்தம் 7.5 CGPA யுடன் 3வது/4வது ஆண்டில் விண்ணப்பிக்கலாம். நிதி உதவி கிடைக்கிறது."
                    }
                }
            },
            
            # Fees & Financial Aid
            {
                "question": "Are there any payment plans available for fee payment?",
                "answer": "Yes, VIT offers flexible payment options: Semester-wise payment, EMI facility through partner banks (0% interest for eligible students), Educational loan assistance, Merit-based fee waivers, Need-based financial aid, and Work-study programs. Payment can be made online, by DD, or through bank transfer.",
                "keywords": ["payment", "EMI", "loan", "installments", "financial", "aid"],
                "category": "fees",
                "languages": {
                    "hi": {
                        "question": "क्या फीस भुगतान के लिए कोई भुगतान योजनाएं उपलब्ध हैं?",
                        "answer": "हां, VIT लचीले भुगतान विकल्प प्रदान करता है: सेमेस्टर-वार भुगतान, साझीदार बैंकों के माध्यम से EMI सुविधा (योग्य छात्रों के लिए 0% ब्याज), शैक्षिक ऋण सहायता, मेधा-आधारित फीस छूट, आवश्यकता-आधारित वित्तीय सहायता, और कार्य-अध्ययन कार्यक्रम। भुगतान ऑनलाइन, DD द्वारा, या बैंक हस्तांतरण के माध्यम से किया जा सकता है।"
                    },
                    "ta": {
                        "question": "கட்டணம் செலுத்துவதற்கு ஏதேனும் பணம் செலுத்தும் திட்டங்கள் உள்ளனவா?",
                        "answer": "ஆம், VIT நெகிழ்வான கட்டண விருப்பங்களை வழங்குகிறது: செமஸ்டர் அடிப்படையிலான கட்டணம், கூட்டாளர் வங்கிகள் மூலம் EMI வசதி (தகுதியான மாணவர்களுக்கு 0% வட்டி), கல்வி கடன் உதவி, தகுதி அடிப்படையிலான கட்டண விலக்கு, தேவை அடிப்படையிலான நிதி உதவி, மற்றும் வேலை-படிப்பு திட்டங்கள். கட்டணம் ஆன்லைன், DD அல்லது வங்கி மாற்றம் மூலம் செலுத்தலாம்."
                    }
                }
            },
            
            # Student Services
            {
                "question": "What health and medical facilities are available on campus?",
                "answer": "VIT provides comprehensive healthcare: 24/7 medical center with qualified doctors and nurses, fully equipped ambulance service, tie-up with nearby hospitals, health insurance for all students, regular health checkups, pharmacy, mental health counseling, emergency medical care, and specialist consultations on appointment.",
                "keywords": ["medical", "health", "doctor", "ambulance", "insurance", "emergency"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "कैंपस में कौन सी स्वास्थ्य और चिकित्सा सुविधाएं उपलब्ध हैं?",
                        "answer": "VIT व्यापक स्वास्थ्य सेवा प्रदान करता है: योग्य डॉक्टरों और नर्सों के साथ 24/7 मेडिकल सेंटर, पूर्ण रूप से सुसज्जित एम्बुलेंस सेवा, आस-पास के अस्पतालों के साथ टाई-अप, सभी छात्रों के लिए स्वास्थ्य बीमा, नियमित स्वास्थ्य जांच, फार्मेसी, मानसिक स्वास्थ्य परामर्श, आपातकालीन चिकित्सा देखभाल, और अपॉइंटमेंट पर विशेषज्ञ परामर्श।"
                    },
                    "ta": {
                        "question": "வளாகத்தில் என்ن சுகாதார மற்றும் மருத்துவ வசதிகள் உள்ளன?",
                        "answer": "VIT விரிவான சுகாதார பராமரிப்பை வழங்குகிறது: தகுதியான மருத்துவர்கள் மற்றும் செவிலியர்களுடன் 24/7 மருத்துவ மையம், முழுமையாக பொருத்தப்பட்ட ஆம்புலன்ஸ் சேவை, அருகிலுள்ள மருத்துவமனைகளுடன் இணைப்பு, அனைத்து மாணவர்களுக்கும் சுகாதார காப்பீடு, வழக்கமான சுகாதார பரிசோதனைகள், மருந்தகம், மன சுகாதார ஆலோசனை, அவசர மருத்துவ பராமரிப்பு, மற்றும் நியமனத்தின் பேரில் நிபுணர் ஆலோசனைகள்."
                    }
                }
            },
            
            {
                "question": "What career guidance and counseling services are provided?",
                "answer": "VIT offers comprehensive career support: Personal career counseling, aptitude testing, resume building workshops, interview preparation sessions, industry mentorship programs, career fairs, internship placement assistance, entrepreneurship guidance, alumni networking events, and psychometric assessments to help students choose right career paths.",
                "keywords": ["career", "counseling", "guidance", "resume", "interview", "mentorship"],
                "category": "placement",
                "languages": {
                    "hi": {
                        "question": "कौन सी कैरियर मार्गदर्शन और परामर्श सेवाएं प्रदान की जाती हैं?",
                        "answer": "VIT व्यापक कैरियर सहायता प्रदान करता है: व्यक्तिगत कैरियर परामर्श, योग्यता परीक्षण, रिज्यूमे निर्माण कार्यशालाएं, साक्षात्कार तैयारी सत्र, उद्योग मार्गदर्शन कार्यक्रम, कैरियर मेले, इंटर्नशिप प्लेसमेंट सहायता, उद्यमिता मार्गदर्शन, पूर्व छात्र नेटवर्किंग इवेंट्स, और छात्रों को सही कैरियर पथ चुनने में मदद के लिए साइकोमेट्रिक आकलन।"
                    },
                    "ta": {
                        "question": "என்ன வாழ்க்கைப் பாதை வழிகாட்டுதல் மற்றும் ஆலோசனை சேவைகள் வழங்கப்படுகின்றன?",
                        "answer": "VIT விரிவான வாழ்க்கைப் பாதை ஆதரவை வழங்குகிறது: தனிப்பட்ட வாழ்க்கைப் பாதை ஆலோசனை, திறன் சோதனை, ரெஸ்யூம் உருவாக்க பட்டறைகள், நேர்காணல் தயாரிப்பு அமர்வுகள், தொழில்துறை வழிகாட்டுதல் திட்டங்கள், வாழ்க்கைப் பாதை கண்காட்சிகள், பயிற்சி இடம்பெறுதல் உதவி, தொழில்முனைவோர் வழிகாட்டுதல், முன்னாள் மாணவர் நெட்வொர்க்கிங் நிகழ்வுகள், மற்றும் மாணவர்கள் சரியான வாழ்க்கைப் பாதையைத் தேர்ந்தெடுக்க உதவும் மனநல மதிப்பீடுகள்."
                    }
                }
            },
            {
                "question": "What are the library operating hours during exams?",
                "answer": "During examination periods, the library extends its hours: Regular days: 8:00 AM to 8:00 PM, Exam period: 7:00 AM to 11:00 PM (Monday-Saturday), Sunday: 9:00 AM to 9:00 PM during exams. Special 24/7 reading rooms are available during final exams with prior registration. Group study rooms can be booked online.",
                "keywords": ["library", "timings", "hours", "exams", "reading", "study", "booking"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "परीक्षा के दौरान पुस्तकालय के संचालन समय क्या हैं?",
                        "answer": "परीक्षा अवधि के दौरान, पुस्तकालय अपने घंटे बढ़ाता है: नियमित दिन: सुबह 8:00 बजे से रात 8:00 बजे तक, परीक्षा अवधि: सुबह 7:00 बजे से रात 11:00 बजे तक (सोमवार-शनिवार), रविवार: परीक्षा के दौरान सुबह 9:00 बजे से रात 9:00 बजे तक। अंतिम परीक्षा के दौरान पूर्व पंजीकरण के साथ विशेष 24/7 पठन कक्ष उपलब्ध हैं। समूह अध्ययन कमरे ऑनलाइन बुक किए जा सकते हैं।"
                    },
                    "ta": {
                        "question": "தேர்வு காலங்களில் நூலக இயக்க நேரங்கள் என்ன?",
                        "answer": "தேர்வு காலங்களில், நூலகம் தனது நேரங்களை நீட்டிக்கிறது: வழக்கமான நாட்கள்: காலை 8:00 முதல் இரவு 8:00 வரை, தேர்வு காலம்: காலை 7:00 முதல் இரவு 11:00 வரை (திங்கள்-சனி), ஞாயிறு: தேர்வுகளின் போது காலை 9:00 முதல் இரவு 9:00 வரை. இறுதித் தேர்வுகளின் போது முன் பதிவுடன் சிறப்பு 24/7 வாசிப்பு அறைகள் கிடைக்கின்றன. குழு படிப்பு அறைகளை ஆன்லைனில் முன்பதிவு செய்யலாம்."
                    }
                }
            },

            {
                "question": "What are the hostel mess timings and food options?",
                "answer": "Hostel mess operates with fixed timings: Breakfast: 7:00 AM to 9:30 AM, Lunch: 12:00 PM to 2:30 PM, Snacks: 4:00 PM to 6:00 PM, Dinner: 7:30 PM to 10:00 PM. Menu includes North Indian, South Indian, and Continental dishes with vegetarian and non-vegetarian options. Special meals during festivals. Monthly mess fees: ₹4,500 (vegetarian), ₹5,200 (non-vegetarian).",
                "keywords": ["hostel", "mess", "food", "timings", "menu", "vegetarian", "fees"],
                "category": "facilities",
                "languages": {
                    "hi": {
                        "question": "छात्रावास मेस का समय और खाना विकल्प क्या हैं?",
                        "answer": "छात्रावास मेस निर्धारित समय के साथ संचालित होता है: नाश्ता: सुबह 7:00 बजे से 9:30 बजे तक, दोपहर का खाना: दोपहर 12:00 बजे से 2:30 बजे तक, स्नैक्स: शाम 4:00 बजे से 6:00 बजे तक, रात का खाना: शाम 7:30 बजे से रात 10:00 बजे तक। मेन्यू में उत्तर भारतीय, दक्षिण भारतीय, और कॉन्टिनेंटल व्यंजन शाकाहारी और मांसाहारी विकल्पों के साथ शामिल हैं। त्योहारों के दौरान विशेष भोजन। मासिक मेस फीस: ₹4,500 (शाकाहारी), ₹5,200 (मांसाहारी)।"
                    },
                    "ta": {
                        "question": "விடுதி உணவகத்தின் நேரம் மற்றும் உணவு விருப்பங்கள் என்ன?",
                        "answer": "விடுதி உணவகம் நிர்ধாரிত நேரத்துடன் இயங்குகிறது: காலை உணவு: காலை 7:00 முதல் 9:30 வரை, மதிய உணவு: மதியம் 12:00 முதல் 2:30 வரை, தின்பண்டங்கள்: மாலை 4:00 முதல் 6:00 வரை, இரவு உணவு: மாலை 7:30 முதல் இரவு 10:00 வரை. மெனுவில் வட இந்திய, தென் இந்திய மற்றும் கான்டினென்டல் உணவுகள் சைவ மற்றும் அசைவ விருப்பங்களுடன் அடங்கும். பண்டிகைகளின் போது சிறப்பு உணவுகள். மாதாந்திர உணவக கட்டணம்: ₹4,500 (சைவம்), ₹5,200 (அசைவம்)."
                    }
                }
            },
            {
                "question": "What are the fee payment deadlines and late fee penalties?",
                "answer": "Fee payment deadlines: Semester fees must be paid by 15th of July (Odd semester) and 15th of January (Even semester). Late fee charges: ₹500 (1-7 days late), ₹1,000 (8-15 days late), ₹2,000 (16-30 days late). After 30 days, students may face academic restrictions. Hostel fees due by 10th of each month. Scholarship recipients get extended deadlines until verification completion.",
                "keywords": ["fee", "deadline", "payment", "late", "penalty", "semester", "hostel"],
                "category": "fees",
                "languages": {
                    "hi": {
                        "question": "फीस भुगतान की अंतिम तिथि और देर से जमा करने पर जुर्माना क्या है?",
                        "answer": "फीस भुगतान की अंतिम तिथि: सेमेस्टर फीस 15 जुलाई (विषम सेमेस्टर) और 15 जनवरी (सम सेमेस्टर) तक जमा करनी होगी। देर से जमा करने पर शुल्क: ₹500 (1-7 दिन देर), ₹1,000 (8-15 दिन देर), ₹2,000 (16-30 दिन देर)। 30 दिन बाद, छात्रों पर शैक्षणिक प्रतिबंध लग सकते हैं। छात्रावास फीस हर महीने की 10 तारीख तक देय है। छात्रवृत्ति प्राप्तकर्ताओं को सत्यापन पूरा होने तक विस्तारित समय सीमा मिलती है।"
                    },
                    "ta": {
                        "question": "கட்டணம் செலுத்தும் கடைசி தேதி மற்றும் தாமதக் கட்டணம் என்ன?",
                        "answer": "கட்டணம் செலுத்தும் கடைசி தேதி: செமஸ்டர் கட்டணம் ஜூலை 15 (ஒற்றைப்படை செமஸ்டர்) மற்றும் ஜனவரி 15 (இரட்டைப்படை செமஸ்டர்) க்குள் செலுத்த வேண்டும். தாமதக் கட்டணங்கள்: ₹500 (1-7 நாட்கள் தாமதம்), ₹1,000 (8-15 நாட்கள் தாமதம்), ₹2,000 (16-30 நாட்கள் தாமதம்). 30 நாட்களுக்குப் பிறகு, மாணவர்களுக்கு கல்வி தடைகள் ஏற்படலாம். விடுதிக் கட்டணம் ஒவ்வொரு மாதமும் 10ஆம் தேதிக்குள் செலுத்த வேண்டும். உதவித்தொகை பெறுபவர்களுக்கு சரிபார்ப்பு முடியும் வரை நீட்டிக்கப்பட்ட கடைசி தேதி கிடைக்கிறது."
                    }
                }
            },
            {
                "question": "What are the different types of scholarships available and their eligibility criteria?",
                "answer": "VIT offers multiple scholarship categories: 1) Merit-based: Academic Excellence (90%+ in 12th) - 100% tuition waiver, High Achievers (85-89%) - 50% waiver, Good Performance (80-84%) - 25% waiver. 2) Government schemes: Central sector scholarship, State government scholarships, SC/ST/OBC scholarships, Minority scholarships. 3) Need-based: Family income <₹2 lakhs - up to 75% fee waiver. 4) Special category: Sports excellence, Cultural talents, Physically challenged students, Defense personnel children. Application deadline: June 30th annually.",
                "keywords": ["scholarships", "merit", "government", "need-based", "eligibility", "criteria", "waiver"],
                "category": "fees",
                "languages": {
                    "hi": {
                        "question": "विभिन्न प्रकार की छात्रवृत्तियां और उनकी पात्रता मानदंड क्या हैं?",
                        "answer": "VIT कई छात्रवृत्ति श्रेणियां प्रदान करता है: 1) मेधा-आधारित: शैक्षणिक उत्कृष्टता (12वीं में 90%+) - 100% ट्यूशन छूट, उच्च प्राप्तकर्ता (85-89%) - 50% छूट, अच्छा प्रदर्शन (80-84%) - 25% छूट। 2) सरकारी योजनाएं: केंद्रीय क्षेत्र छात्रवृत्ति, राज्य सरकार छात्रवृत्ति, SC/ST/OBC छात्रवृत्ति, अल्पसंख्यक छात्रवृत्ति। 3) आवश्यकता-आधारित: पारिवारिक आय <₹2 लाख - 75% तक फीस छूट। 4) विशेष श्रेणी: खेल उत्कृष्टता, सांस्कृतिक प्रतिभा, शारीरिक रूप से चुनौतीग्रस्त छात्र, रक्षा कर्मियों के बच्चे। आवेदन की अंतिम तिथि: वार्षिक 30 जून।"
                    },
                    "ta": {
                        "question": "பல்வேறு வகையான உதவித்தொகைகள் மற்றும் அவற்றின் தகுதி அளவுகோல்கள் என்ன?",
                        "answer": "VIT பல உதவித்தொகை வகைகளை வழங்குகிறது: 1) தகுதி அடிப்படை: கல்வி சிறப்பு (12வதில் 90%+) - 100% கல்விக் கட்டண விலக்கு, உயர் சாதனையாளர்கள் (85-89%) - 50% விலக்கு, நல்ல செயல்பாடு (80-84%) - 25% விலக்கு। 2) அரசாங்க திட்டங்கள்: மத்திய துறை உதவித்தொகை, மாநில அரசு உதவித்தொகைகள், SC/ST/OBC உதவித்தொகைகள், சிறுபான்மை உதவித்தொகைகள். 3) தேவை அடிப்படை: குடும்ப வருமானம் <₹2 லட்சம் - 75% வரை கட்டண விலக்கு। 4) சிறப்பு வகை: விளையாட்டு சிறப்பு, கலாச்சார திறமைகள், உடல் ஊனமுற்ற மாணவர்கள், பாதுகாப்பு பணியாளர்களின் குழந்தைகள். விண்ணப்ப கடைசி தேதி: ஆண்டுதோறும் ஜூன் 30."
                    }
                }
            }
        ]
        
        for item in sample_faqs:
            faq = FAQ(**item)
            await db.insert_faq(faq)