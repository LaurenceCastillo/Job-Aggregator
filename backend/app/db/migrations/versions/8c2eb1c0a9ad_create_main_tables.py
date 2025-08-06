"""create_main_tables
 
Revision ID: 8c2eb1c0a9ad
Revises: 
Create Date: 2025-07-30 01:20:12.018872
 
"""
from alembic import op
import sqlalchemy as sa

 
# revision identifiers, used by Alembic
revision = '8c2eb1c0a9ad'
down_revision = None
branch_labels = None
depends_on = None
 
def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"), #server_default states default column value which is enforced by the server
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def create_profile_table() -> None:
    pass

def create_user_skills_table() -> None:
    pass
def create_user_interests_table() -> None:
    pass
def create_preferred_locations_table() -> None:
    pass
def create_search_history_table() -> None:
    pass
def create_clicked_jobs_table() -> None:
    pass
 
def upgrade() -> None:
    create_cleanings_table()
 
 
def downgrade() -> None:
    op.drop_table("cleanings")
 
 