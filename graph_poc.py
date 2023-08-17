from neo4j import GraphDatabase
from adversary_generator import AdversaryGenerator
from attachments_generator import AttachmentGenerator
from event_generator import EventGenerator
from indicator_generator import IndicatorGenerator
from signature_generator import SignatureGenerator
from source_generator import SourceGenerator
import sys


# Define the Neo4j URI and credentials
uri = "bolt://localhost:7687"  # Change this to your Neo4j URI
username = "neo4j"
password = "password"  # Change this to your Neo4j password

def create_indicators_in_batch(tx, batch_data):
    query = """
    UNWIND $batchData AS data
    CREATE (:Indicator {
        indicator_value: data.indicator_value,
        indicator_type_name: data.indicator_value,
        indicator_status_name: data.indicator_status_name,
        indicator_hash: data.indicator_hash,
        indicator_score: data.indicator_score,
        indicator_touched_at: data.indicator_touched_at,
        indicator_generated_score: data.indicator_generated_score,
        related_exploit_target_count: data.related_exploit_target_count,
        indicator_updated_at: data.indicator_updated_at,
        indicator_published_at: data.indicator_published_at,
        related_task_count: data.related_task_count,
        related_adversary_count: data.related_adversary_count,
        related_investigation_count: data.related_investigation_count,
        related_vulnerability_count: data.related_vulnerability_count,
        indicator_created_at: data.indicator_created_at,
        related_tool_count: data.related_tool_count,
        related_signature_count: data.related_signature_count,
        related_indicator_count: data.related_indicator_count,
        related_ttp_count: data.related_ttp_count,
        related_campaign_count: data.related_campaign_count,
        indicator_type_id: data.indicator_type_id,
        indicator_id: data.indicator_id,
        related_malware_count: data.related_malware_count,
        related_attack_pattern_count: data.related_attack_pattern_count,
        related_attachment_count: data.related_attachment_count,
        related_event_count: data.related_event_count,
        related_report_count: data.related_report_count,
        doc_type: data.doc_type,
        related_asset_count: data.related_asset_count,
        related_identity_count: data.related_identity_count,
        indicator_status_id: data.indicator_status_id,
        related_course_of_action_count: data.related_course_of_action_count,
        doc_id: data.doc_id,
        related_intrusion_set_count: data.related_intrusion_set_count,
        related_incident_count: data.related_incident_count
    })
    """
    tx.run(query, batchData=batch_data)

def create_adversaries_in_batch(tx, batch_data):
    query = """
    UNWIND $batchData AS data
    CREATE (:Adversary {
        adversary_name: data.adversary_name,
        related_exploit_target_count: data.related_exploit_target_count,
        related_task_count: data.related_task_count,
        related_adversary_count: data.related_adversary_count,
        related_investigation_count: data.related_investigation_count,
        related_vulnerability_count: data.related_vulnerability_count,
        related_tool_count: data.related_tool_count,
        related_signature_count: data.related_signature_count,
        related_indicator_count: data.related_indicator_count,
        adversary_created_at: data.adversary_created_at,
        related_ttp_count: data.related_ttp_count,
        related_campaign_count: data.related_campaign_count,
        related_malware_count: data.related_malware_count,
        related_attack_pattern_count: data.related_attack_pattern_count,
        adversary_touched_at: data.adversary_touched_at,
        related_attachment_count: data.related_attachment_count,
        adversary_updated_at: data.adversary_updated_at,
        related_event_count: data.related_event_count,
        related_report_count: data.related_report_count,
        adversary_published_at: data.adversary_published_at,
        doc_type: data.doc_type,
        adversary_id: data.adversary_id,
        related_asset_count: data.related_asset_count,
        related_identity_count: data.related_identity_count,
        related_course_of_action_count: data.related_course_of_action_count,
        doc_id: data.doc_id,
        related_intrusion_set_count: data.related_intrusion_set_count,
        related_incident_count: data.related_incident_count
    })
    """
    tx.run(query, batchData=batch_data)

def create_events_in_batch(tx, batch_data):
    query = """
    UNWIND $batchData AS data
    CREATE (:Event {
        adversary_name: data.adversary_name,
        related_exploit_target_count: data.related_exploit_target_count,
        related_task_count: data.related_task_count,
        related_adversary_count: data.related_adversary_count,
        related_investigation_count: data.related_investigation_count,
        related_vulnerability_count: data.related_vulnerability_count,
        related_tool_count: data.related_tool_count,
        related_signature_count: data.related_signature_count,
        related_indicator_count: data.related_indicator_count,
        adversary_created_at: data.adversary_created_at,
        related_ttp_count: data.related_ttp_count,
        related_campaign_count: data.related_campaign_count,
        related_malware_count: data.related_malware_count,
        related_attack_pattern_count: data.related_attack_pattern_count,
        adversary_touched_at: data.adversary_touched_at,
        related_attachment_count: data.related_attachment_count,
        adversary_updated_at: data.adversary_updated_at,
        related_event_count: data.related_event_count,
        related_report_count: data.related_report_count,
        adversary_published_at: data.adversary_published_at,
        doc_type: data.doc_type,
        adversary_id: data.adversary_id,
        related_asset_count: data.related_asset_count,
        related_identity_count: data.related_identity_count,
        related_course_of_action_count: data.related_course_of_action_count,
        doc_id: data.doc_id,
        related_intrusion_set_count: data.related_intrusion_set_count,
        related_incident_count: data.related_incident_count
    })
    """
    tx.run(query, batchData=batch_data)


batch_size = 5000
indicator_index = 0

# Connect to the Neo4j database
driver = GraphDatabase.driver(uri, auth=(username, password))

 
sys.argv.append("1")

if sys.argv[1] == "1":    
    indicator_index = 0
    indicatorGenerator = IndicatorGenerator()
    with driver.session() as session:
        for i in range(0, 20000000, batch_size):
            print(f"batch {i} from indicator started")
            indicator_data = indicatorGenerator.generate_objects(batch_size,indicator_index)        
            session.execute_write(create_indicators_in_batch, indicator_data)
            indicator_index +=  batch_size

if sys.argv[1] == "2":    
    adversary_index = 0
    adversaryGenerator = AdversaryGenerator()
    with driver.session() as session:
        for i in range(0, 20000000, batch_size):
            print(f"batch {i} from adversaries started")
            adversary_data = adversaryGenerator.generate_objects(batch_size,adversary_index)        
            session.execute_write(create_adversaries_in_batch, adversary_data)
            indicator_index +=  batch_size

if sys.argv[1] == "3":    
    event_index = 0
    eventGenerator = EventGenerator()
    with driver.session() as session:
        for i in range(0, 40000000, batch_size):
            print(f"batch {i} from events started")
            adversary_data = eventGenerator.generate_objects(batch_size,event_index)        
            session.execute_write(create_events_in_batch, adversary_data)
            indicator_index +=  batch_size




# Close the driver when done
driver.close()

