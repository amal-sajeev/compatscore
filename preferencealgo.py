from pydantic import BaseModel

class HinduAttributes:
    gotra: str = None
    rashi: str = None
    manglik_status: str = None  # "yes", "no", "anshik", "dont_know"
    nakshatra: str = None


class MuslimAttributes:
    sect: str = None  # "sunni", "shia", "other"
    perform_namaz: str = None  # "five_times", "occasionally", "only_jumma", "no"
    observe_ramadan: bool = None 
    religious_practice: str = None  # "practicing", "moderate", "liberal"


class SikhAttributes:
    amritdhari: bool = None 
    clean_shaven: bool = None 

class ChristianAttributes:
    denomination: str = None
    church_involvement: str = None  # "very_active", "somewhat_active", "rarely", "never"

class ReligiousInfo:
    religion: str = None  # "hindu", "muslim", "christian", "sikh", "buddhist", "jain", "parsi", "jewish", "other"
    community: str = None  # "brahmin", "kshatriya", "vaishya", "shudra", etc.
    sub_community: str = None
    mother_tongue: str = None  # "hindi", "english", "tamil", "bengali", etc.
    gothra: str = None
    caste: str = None
    sub_caste: str = None
    manglik: str = None  # "yes", "no", "anshik", "dont_know"
    nakshatra: str = None
    religious_values: str = None  # "traditional", "moderate", "liberal"
    
    # Religion-specific attributes (conditional based on religion)
    hindu_attributes:  hindu_attibutes = None
    muslim_attributes: muslim_attributes = None
    sikh_attributes: sikh_attributes = None
    christian_attributes: sikh_attributes = None

class FamilyDetail:
    family_type: str = None  # "joint", "nuclear", "extended"
    family_status: str = None  # "middle_class", "upper_middle_class", "rich", "affluent"
    family_values: str = None  # "traditional", "moderate", "liberal"
    father_occupation: str = None
    mother_occupation: str = None
    brothers: int = None
    brothers_married: int = None
    sisters: int = None
    sisters_married: int = None
    family_location: str = None
    about_family: str = None

# Education Information
class EducationDetail:
    highest_education: str = None  # "high_school", "diploma", "bachelors", "masters", "doctorate", "professional"
    education_field: str = None  # "engineering", "medicine", "commerce", "arts", etc.
    college_name: str = None
    year_of_passing: int = None
    additional_qualification: str = None

# Career Information
class CareerDetail:
    occupation: str = None  # "private_sector", "government", "business", "self_employed", "doctor", "engineer", "teacher", "not_working", "other"
    occupation_detail: str = None  # Specific job title
    employer_name: str = None
    annual_income: float = None  # 500000.00
    income_currency: str = None  # "INR", "USD", etc.
    work_location: str = None

# Location Information
class Location_Info:
    country: str = None  # "India", "USA", "Canada", etc.
    state: str = None  # "Maharashtra", "California", etc.
    city: str = None  # "Mumbai", "San Francisco", etc.
    pincode: str = None
    residential_status: str = None  # "citizen", "permanent_resident", "work_permit", "student_visa", "temporary_visa"
    current_residence: str = None
    hometown: str = None
    willing_to_relocate: bool = None

# Lifestyle Information
class Lifestyle:
    diet: str = None  # "veg", "non_veg", "eggetarian", "vegan", "jain"
    smoking: str = None  # "never", "occasionally", "regularly"
    drinking: str = None  # "never", "occasionally", "regularly"
    pets: str = None  # "love_pets", "dont_like_pets", "have_pets", "no_pets"
    own_house: bool = None
    own_car: bool = None
    hobbies: str = None  # Comma-separated: "reading, traveling, cooking"
    interests: str = None # Comma-separated: "music, sports, movies"


# Partner Preferences
class PartnerPreferences:
    age_min: int = None  # 25
    age_max: int = None  # 35
    height_min_cm: int = None  # 160
    height_max_cm: int = None  # 180
    marital_status: str = None  # Comma-separated: "never_married,divorced"
    religions: str = None  # Comma-separated: "hindu,sikh"
    castes: str = None  # Comma-separated list
    mother_tongues: str = None  # Comma-separated: "hindi,english"
    education_level: str = None  # Comma-separated: "bachelors,masters,doctorate"
    profession: str = None  # Comma-separated: "doctor,engineer,business"
    annual_income_min: float = None  # 300000.00
    diet_preference: str = None  # Comma-separated: "veg,eggetarian"
    smoking_preference: str = None  # "doesnt_matter", "never", "occasionally", "regularly"
    drinking_preference: str = None  # "doesnt_matter", "never", "occasionally", "regularly"
    preferred_countries: str = None  # Comma-separated: "India,USA"
    preferred_states: str = None  # Comma-separated: "Maharashtra,Karnataka"
    preferred_cities: str = None  # Comma-separated: "Mumbai,Pune"
    manglik_preference: str = None  # "yes", "no", "doesnt_matter"
    descriptions: str = None # Free text about partner expectations


# Profile Media
class ProfilePhoto:
    
    photo_id: int = None
    photo_url: str = None
    is_primary: bool = None
    is_verified: bool = None
    visibility: str = None # "all", "connections", "accepted_interests"


# Horoscope Information (optional)
class Horoscope:
    birth_date: str = None  # "1995-03-15"
    birth_time: str = None  # "14:30:00"
    birth_place: str = None  # "Mumbai, Maharashtra, India"
    horoscope_image_url: str = None
    manglik: str = None  # "yes", "no", "anshik", "dont_know"
    astrological_details: str = None

class Metadata:
    religion_weight: float
    community_weight: float
    education_weight: float
    profession_weight: float
    location_weight: float
    age_weight: float
    lifestyle_weight: float

class Profile:
    user_id: int
    profile_id: int
    email: str
    phone_number: str
    registration_date: str  # ISO format: "2024-01-15T10:30:00Z"
    account_status: str  # "active", "inactive", "suspended", "verified"
    verification_status: str  # "pending", "verified", "rejected"
    membership_type: str  # "free", "premium", "gold", "platinum"
    profile_completion_percentage: int  # 0-100
    
    # Personal Information
    profile_for: str  # "self", "son", "daughter", "brother", "sister", "relative", "friend"
    first_name: str = None
    last_name: str
    gender: str  # "male", "female", "other"
    date_of_birth: str  # "1995-03-15"
    age: int  # Auto-calculated
    marital_status: str  # "never_married", "widowed", "divorced", "awaiting_divorce"
    height_cm: int = None  # 165
    weight_kg: int = None  # 65
    body_type: str = None  # "slim", "athletic", "average", "heavy"
    complexion: str = None  # "very_fair", "fair", "wheatish", "wheatish_brown", "dark"
    blood_group: str = None  # "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"
    differently_abled: bool
    differently_abled_details: str = None
    health_conditions: str = None
    profile_headline: str = None
    about_me: str = None
    verified_id: bool = None
    verified_photo: bool = None
    show_horoscope: bool = Falsed
    religious_info: ReligiousInfo = None
    family_details: FamilyDetail = None
    education_details: EducationDetail = None
    career_detail: CareerDetail = None
    location_info: Location_Info = None
    lifestyle: Lifestyle = None
    partner_preferences: PartnerPreferences = None
    profile_photos: ProfilePhoto = None
    horoscope: Horoscope = None 
    metadata: Metadata

def demographic_match(profile1: Profile, profile2: Profile):
    """ Compares demographic details from both user profiles and creates various scores that will be used to calculate the demographic score.

    Args:
        profile1 (Profile): First user Profile
        profile2 (Profile): Second user Profile         
    """ 
    age_diff = abs(profile1.age - profile2.age)
    age_score = max(0, 100 - (age_diff * 3)) #max() to arevent score from becoming negative

    #Height Compatibility
    height_diff = abs(profile1.height_cm-profile2.height_cm)
    height_score = max(0,100 - (height_diff*0.5))
    demographic_score = (age_score+height_score)/2  

def cultural_match(profile1:Profile, profile2: Profile):
    """Compares religions and cultural details from    ofiles and creates various scores that will be used to calculate the cultural match score.

    Args:
        profile1 (Profile): First user Profile
        profile2 (Profile): Second user Profile
    """
    #Religious match
    # if profile1.religious_info.


    