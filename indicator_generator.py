from faker import Faker
import random
from datetime import datetime
import json

from source_generator import SourceGenerator

class IndicatorGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects,startindex):
        objects = []

        source_generator = SourceGenerator()

        for j in range(1, num_objects + 1):
            obj = {
                "indicator_value": self.faker.domain_name(),
                "indicator_type_name": "FQDN",
                "indicator_status_name": random.choice(["Review", "Active", "Inactive"]),
                "indicator_hash": self.faker.md5(),
                "indicator_score": round(random.uniform(0, 10), 2),
                "indicator_touched_at": datetime.utcnow().isoformat() + "Z",
                "indicator_generated_score": round(random.uniform(0, 10), 2),
                "related_exploit_target_count": random.randint(0, 10),
                "indicator_updated_at": datetime.utcnow().isoformat() + "Z",
                "indicator_published_at": datetime.utcnow().isoformat() + "Z",
                "related_task_count": random.randint(0, 10),
                "related_adversary_count": random.randint(0, 10),
                "related_investigation_count": random.randint(0, 10),
                "related_vulnerability_count": random.randint(0, 10),
                "indicator_created_at": datetime.utcnow().isoformat() + "Z",
                "related_tool_count": random.randint(0, 10),
                "related_signature_count": random.randint(0, 10),
                "related_indicator_count": random.randint(0, 10),
                "related_ttp_count": random.randint(0, 10),
                "related_campaign_count": random.randint(0, 10),
                "indicator_type_id": random.randint(1, 20),
                "indicator_id": random.randint(1, 100),
                "related_malware_count": random.randint(0, 10),
                "related_attack_pattern_count": random.randint(0, 10),
                "related_attachment_count": random.randint(0, 10),
                "related_event_count": random.randint(0, 10),
                "related_report_count": random.randint(0, 10),
                "doc_type": "indicator",
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "indicator_status_id": random.randint(1, 5),
                "related_course_of_action_count": random.randint(0, 10),
                "doc_id": f"indicator_{startindex}",
                "related_intrusion_set_count": random.randint(0, 10),                
                "related_incident_count": random.randint(0, 10)                    
            }

            startindex+=1

           
            objects.append(obj)

        return objects

