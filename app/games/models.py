from sqlalchemy import Boolean, Column, Float, Integer, String, ForeignKey, DateTime
from app.database import Base
from datetime import datetime

class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String, index=True)
    slug = Column(String)
    aggregated_rating = Column(Float)
    aggregated_rating_count = Column(Integer)
    igdb_rating = Column(Float)
    igdb_rating_count = Column(Integer)
    total_rating = Column(Float)
    total_rating_count = Column(Integer)
    game_type = Column(Integer, ForeignKey("game_types.id"))
    game_status = Column(Integer, ForeignKey("game_statuses.id"))
    storyline = Column(String)
    summary = Column(String)
    parent_game = Column(Integer, ForeignKey("games.id"))
    version_parent = Column(Integer, ForeignKey("games.id"))
    version_title = Column(String)
    cover = Column(Integer, ForeignKey("covers.id"))
    first_release_date = Column(Integer) # Unix timestamp
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Covers(Base):
    __tablename__ = "covers"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    game_localization = Column(Integer, ForeignKey("game_localizations.id"))
    url = Column(String)
    alpha_channel = Column(Boolean)
    animated = Column(Boolean)
    height = Column(Integer)
    width = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameLocalizations(Base):
    __tablename__ = "game_localizations"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    game_id = Column(Integer, ForeignKey("games.id"))
    cover_id = Column(Integer, ForeignKey("covers.id"))
    region_id = Column(Integer, ForeignKey("regions.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Regions(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    category = Column(String)
    indentifier = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Companies(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    slug = Column(String)
    name = Column(String)
    description = Column(String)
    country = Column(Integer)
    logo_url = Column(String)
    parent_id = Column(Integer, ForeignKey("companies.id"))
    status_id = Column(Integer, ForeignKey("company_statuses.id"))
    url = Column(String)
    start_date = Column(Integer) # Unix timestamp
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class InvolvedCompanies(Base):
    __tablename__ = "involved_companies"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    developer = Column(Boolean)
    publisher = Column(Boolean)
    porting = Column(Boolean)
    supporting = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class CompanyStatuses(Base):
    __tablename__ = "company_statuses"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameEngines(Base):
    __tablename__ = "game_engines"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    description = Column(String)
    logo_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameEnginesCompanies(Base):
    __tablename__ = "game_engines_companies"

    game_engine_id = Column(Integer, ForeignKey("game_engines.id"), primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), primary_key=True)


class GameEnginesGames(Base):
    __tablename__ = "game_engines_games"

    game_engine_id = Column(Integer, ForeignKey("game_engines.id"), primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)


class GameStatuses(Base):
    __tablename__ = "game_statuses"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameTypes(Base):
    __tablename__ = "game_types"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    type = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameTimeToBeat(Base):
    __tablename__ = "game_time_to_beat"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    hastily = Column(Integer)
    normally = Column(Integer)
    completely = Column(Integer)
    submissions_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Franchises(Base):
    __tablename__ = "franchises"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class FranchiseGames(Base):
    __tablename__ = "franchise_games"

    franchise_id = Column(Integer, ForeignKey("franchises.id"), primary_key=True)
    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)


class Genres(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameGenres(Base):
    __tablename__ = "game_genres"

    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id"), primary_key=True)


class Keywords(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameKeywords(Base):
    __tablename__ = "game_keywords"

    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    keyword_id = Column(Integer, ForeignKey("keywords.id"), primary_key=True)


class Themes(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameThemes(Base):
    __tablename__ = "game_themes"

    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    theme_id = Column(Integer, ForeignKey("themes.id"), primary_key=True)


class AgeRatings(Base):
    __tablename__ = "age_ratings"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    rating_category = Column(Integer, ForeignKey("age_rating_categories.id"))
    content_descriptions = Column(Integer, ForeignKey("age_rating_content_descriptions.id"))
    rating_content_descriptions = Column(Integer, ForeignKey("age_rating_content_descriptions_v2.id"))
    organization = Column(Integer, ForeignKey("age_rating_organizations.id"))
    rating_cover_url = Column(String)
    synopsis = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class AgeRatingCategories(Base):
    __tablename__ = "age_rating_categories"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    rating = Column(String)
    organization = Column(Integer, ForeignKey("age_rating_organizations.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class AgeRatingContentDescriptions(Base):
    __tablename__ = "age_rating_content_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class AgeRatingContentDescriptionsV2(Base):
    __tablename__ = "age_rating_content_descriptions_v2"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    description = Column(String)
    organization = Column(Integer, ForeignKey("age_rating_organizations.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class AgeRatingOrganizations(Base):
    __tablename__ = "age_rating_organizations"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GamesAgeRatings(Base):
    __tablename__ = "games_age_ratings"

    game_id = Column(Integer, ForeignKey("games.id"), primary_key=True)
    age_rating_id = Column(Integer, ForeignKey("age_ratings.id"), primary_key=True)
    

class AlternativeNames(Base):
    __tablename__ = "alternative_names"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    name = Column(String)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Artworks(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    url = Column(String)
    alpha_channel = Column(Boolean)
    animated = Column(Boolean)
    height = Column(Integer)
    width = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Screenshots(Base):
    __tablename__ = "screenshots"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    url = Column(String)
    alpha_channel = Column(Boolean)
    animated = Column(Boolean)
    height = Column(Integer)
    width = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameVideos(Base):
    __tablename__ = "game_videos"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    name = Column(String)
    video_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class Platforms(Base):
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    abbreviation = Column(String)
    alternative_name = Column(String)
    name = Column(String)
    slug = Column(String)
    generation = Column(Integer)
    platform_logo_url = Column(String)
    platform_family = Column(Integer, ForeignKey("platform_families.id"))
    platform_type = Column(Integer, ForeignKey("platform_types.id"))
    summary = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class PlatformFamilies(Base):
    __tablename__ = "platform_families"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    slug = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class PlatformTypes(Base):
    __tablename__ = "platform_types"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class GameEnginesPlatforms(Base):
    __tablename__ = "game_engines_platforms"

    game_engine_id = Column(Integer, ForeignKey("game_engines.id"), primary_key=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"), primary_key=True)


class ReleaseDates(Base):
    __tablename__ = "release_dates"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    release_region = Column(Integer, ForeignKey("release_date_regions.id"))
    date = Column(DateTime)
    readable_date = Column(String)
    release_month = Column(Integer)
    release_year = Column(Integer)
    status = Column(Integer, ForeignKey("release_date_statuses.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class ReleaseDateRegions(Base):
    __tablename__ = "release_date_regions"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    region = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)


class ReleaseDateStatuses(Base):
    __tablename__ = "release_date_statuses"

    id = Column(Integer, primary_key=True, index=True)
    igdb_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)