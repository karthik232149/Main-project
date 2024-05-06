# Generated by Django 4.0.1 on 2024-04-16 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('EmaiL', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=100)),
                ('Pin', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('Gender', models.CharField(max_length=100)),
                ('Photo', models.CharField(max_length=500)),
                ('PLACE', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.login')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('EmaiL', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=100)),
                ('Pin', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('Gender', models.CharField(max_length=100)),
                ('Photo', models.CharField(max_length=500)),
                ('PLACE', models.CharField(max_length=100)),
                ('Status', models.CharField(default='pending', max_length=20)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.login')),
            ],
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
                ('TRAINER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('TRAINER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.trainer')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.user')),
            ],
        ),
        migrations.CreateModel(
            name='Health_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Height', models.CharField(max_length=100)),
                ('Weight', models.CharField(max_length=100)),
                ('Age', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(default='', max_length=100)),
                ('Obesity', models.CharField(max_length=100)),
                ('Blood_pressure', models.CharField(max_length=100)),
                ('Diabetes', models.CharField(max_length=100)),
                ('Cholesterol', models.CharField(max_length=100)),
                ('Alcohol_use', models.CharField(max_length=100)),
                ('Drug_use', models.CharField(max_length=100)),
                ('Smoking', models.CharField(max_length=100)),
                ('Headaches', models.CharField(max_length=100)),
                ('Asthma', models.CharField(max_length=100)),
                ('Heart_problems', models.CharField(max_length=100)),
                ('Cancer', models.CharField(max_length=100)),
                ('Stroke', models.CharField(max_length=100)),
                ('Bone_joint', models.CharField(max_length=100)),
                ('Kidney_problem', models.CharField(max_length=100)),
                ('Liver_problems', models.CharField(max_length=100)),
                ('Depression', models.CharField(max_length=100)),
                ('Allergies', models.CharField(max_length=100)),
                ('Arthritis', models.CharField(max_length=100)),
                ('Pregnancy', models.CharField(max_length=100)),
                ('Bmi', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.user')),
            ],
        ),
        migrations.CreateModel(
            name='Diet_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('menu', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('TRAINER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Diet_chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Height', models.CharField(max_length=100)),
                ('Weight', models.CharField(max_length=100)),
                ('Age', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(default='', max_length=100)),
                ('Obesity', models.CharField(max_length=100)),
                ('Blood_pressure', models.CharField(max_length=100)),
                ('Diabetes', models.CharField(max_length=100)),
                ('Cholesterol', models.CharField(max_length=100)),
                ('Alcohol_use', models.CharField(max_length=100)),
                ('Drug_use', models.CharField(max_length=100)),
                ('Smoking', models.CharField(max_length=100)),
                ('Headaches', models.CharField(max_length=100)),
                ('Asthma', models.CharField(max_length=100)),
                ('Heart_problems', models.CharField(max_length=100)),
                ('Cancer', models.CharField(max_length=100)),
                ('Stroke', models.CharField(max_length=100)),
                ('Bone_joint', models.CharField(max_length=100)),
                ('Kidney_problem', models.CharField(max_length=100)),
                ('Liver_problems', models.CharField(max_length=100)),
                ('Depression', models.CharField(max_length=100)),
                ('Allergies', models.CharField(max_length=100)),
                ('Arthritis', models.CharField(max_length=100)),
                ('Pregnancy', models.CharField(max_length=100)),
                ('Bmi', models.CharField(max_length=100)),
                ('Date', models.CharField(default='', max_length=100)),
                ('menu', models.CharField(default='', max_length=100)),
                ('quantity', models.CharField(default='', max_length=100)),
                ('Time', models.CharField(max_length=100)),
                ('TRAINER', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('reply', models.CharField(max_length=100)),
                ('Status', models.CharField(default='pending', max_length=20)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ai_yoga_pose.user')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('FROMID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_id', to='Ai_yoga_pose.login')),
                ('TOID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_id', to='Ai_yoga_pose.login')),
            ],
        ),
    ]
