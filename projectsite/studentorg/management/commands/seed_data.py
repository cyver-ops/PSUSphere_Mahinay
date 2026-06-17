import random
from datetime import date
from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Populate the application database with a robust mix of actual structures and voluminous dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing existing memberships and student data...'))
        # Clear out dependent relation tables first to ensure clean execution states
        OrgMember.objects.all().delete()
        Student.objects.all().delete()
        Organization.objects.all().delete()

        # Step 1: Ensure Core Structures Exist
        self.ensure_base_academic_structures()

        # Step 2: Generate Voluminous Balanced Dummy Data
        self.stdout.write(self.style.WARNING('\nGenerating comprehensive dummy database entries...'))
        self.seed_dummy_organizations(15)
        self.seed_dummy_students(150)  # Generates a realistic pool of 150 unique students
        self.seed_dummy_memberships(80) # Cross-links students into random campus orgs

        self.stdout.write(self.style.SUCCESS(
            '\n[SUCCESS] Master database seeding completed! Your premium UI tables are now fully populated.'
        ))

    def ensure_base_academic_structures(self):
        """Ensures the official structural academic ecosystem exists in the database"""
        # 1. Populate Colleges
        colleges = [
            'College of Science', 'College of Engineering', 'College of Teacher Education',
            'College of Nursing and Health', 'College of Arts and Humanities',
            'College of Business and Accountancy', 'College of Hospitality and Tourism Management',
            'College of Architecture and Design'
        ]
        for name in colleges:
            College.objects.get_or_create(college_name=name)
        
        # 2. Populate Programs
        programs = [
            ('Bachelor of Science in Computer Science', 'College of Science'),
            ('Bachelor of Science in Information Technology', 'College of Science'),
            ('Bachelor of Science in Civil Engineering', 'College of Engineering'),
            ('Bachelor of Secondary Education Major in Mathematics', 'College of Teacher Education'),
            ('Bachelor of Elementary Education', 'College of Teacher Education'),
            ('Bachelor of Science in Nursing', 'College of Nursing and Health'),
            ('Bachelor of Arts in Political Science', 'College of Arts and Humanities'),
            ('Bachelor of Science in Accountancy', 'College of Business and Accountancy'),
            ('Bachelor of Science in Tourism Management', 'College of Hospitality and Tourism Management'),
            ('Bachelor of Science in Architecture', 'College of Architecture and Design'),
        ]
        for prog_name, college_name in programs:
            college = College.objects.filter(college_name=college_name).first()
            if college:
                Program.objects.get_or_create(prog_name=prog_name, college=college)

        self.stdout.write(self.style.SUCCESS('✓ Standard Colleges and Programs verified in database.'))

    def seed_dummy_organizations(self, count):
        """Generates dynamic academic and special interest campus student organizations"""
        fake = Faker()
        suffixes = ['Society', 'Alliance', 'Guild', 'Association', 'Council', 'Club']
        
        # Seed your requested mandatory actual org entries safely first
        cs_college = College.objects.filter(college_name='College of Science').first()
        Organization.objects.get_or_create(name='ACS', defaults={'college': cs_college, 'description': 'Association of Computer Scientists'})
        Organization.objects.get_or_create(name='SITE', defaults={'college': cs_college, 'description': 'Society of Information Technology Enthusiasts'})

        for _ in range(count):
            random_college = College.objects.order_by('?').first()
            if not random_college:
                continue
                
            # Formulate clean, realistic campus organizational titles
            keyword = fake.word().title()
            suffix = random.choice(suffixes)
            org_title = f"{keyword} Student {suffix}"

            Organization.objects.create(
                name=org_title,
                college=random_college,
                description=f"Official student body registry for individuals interested in {keyword.lower()} processing systems."
            )
        self.stdout.write(self.style.SUCCESS(f'✓ Created {count} high-contrast Organization profiles.'))

    def seed_dummy_students(self, count):
        """Generates voluminous student entries using realistic regional Philippine formatting parameters"""
        fake = Faker('en_PH')  # Matches your project's regional locale parameters cleanly
        all_programs = list(Program.objects.all())

        if not all_programs:
            return

        for _ in range(count):
            random_program = random.choice(all_programs)
            
            # Formulates dynamic student IDs matching your precise structural requirements (e.g. 2024-8-4105)
            year_prefix = fake.random_int(2021, 2026)
            branch_id = fake.random_int(1, 8)
            sequence_num = fake.random_number(digits=4, fix_len=True)
            generated_id = f"{year_prefix}-{branch_id}-{sequence_num}"

            # Respects the case-sensitive exact naming dictionary expected by your models.py layer
            Student.objects.create(
                student_id=generated_id,
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random_program
            )
        self.stdout.write(self.style.SUCCESS(f'✓ Injected {count} unique student records into the system.'))

    def seed_dummy_memberships(self, count):
        """Cross-references random students to organizations to build out the many-to-many lookup tables"""
        fake = Faker()
        students_pool = list(Student.objects.all())
        orgs_pool = list(Organization.objects.all())

        if not students_pool or not orgs_pool:
            return

        seeded = 0
        for _ in range(count):
            random_student = random.choice(students_pool)
            random_org = random.choice(orgs_pool)

            # Prevent duplication issues across the relational lookup layer
            exists = OrgMember.objects.filter(student=random_student, organization=random_org).exists()
            if not exists:
                OrgMember.objects.create(
                    student=random_student,
                    organization=random_org,
                    date_joined=fake.date_between(start_date="-3y", end_date="today")
                )
                seeded += 1
                
        self.stdout.write(self.style.SUCCESS(f'✓ Linked {seeded} active Student Organizational memberships.'))