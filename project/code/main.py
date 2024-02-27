from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import logging
import os

class ActionStrategy:
    def execute(self, calendar_service, **kwargs):
        pass

class RequestEventActionStrategy(ActionStrategy):
    def execute(self, calendar_service, **kwargs):
        title = input("Digite o título do evento: ")
        date_str = input("Digite a data do evento (formato YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        event = {
            'summary': title,
            'start': {
                'dateTime': date.isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (date + datetime.timedelta(hours=1)).isoformat(),
                'timeZone': 'UTC',
            },
        }

        calendar_service.service.events().insert(
            calendarId='primary',
            body=event
        ).execute()

        calendar_service.logger.info(f"Requested a new event - Title: {title}, Date: {date}")

class CancelEventActionStrategy(ActionStrategy):
    def execute(self, calendar_service, **kwargs):
        # Adicione lógica para cancelar um agendamento
        calendar_service.logger.info('Canceled an event.')

class RescheduleEventActionStrategy(ActionStrategy):
    def execute(self, calendar_service, **kwargs):
        # Adicione lógica para remarcar um agendamento
        calendar_service.logger.info('Rescheduled an event.')

# Contexto para escolher a estratégia correta
class EventProcessorContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_events(self, calendar_service, **kwargs):
        self.strategy.execute(calendar_service, **kwargs)

class GoogleCalendarService:
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.scopes = ['https://www.googleapis.com/auth/calendar']
        self.service = self.build_service()
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger('google_calendar_app')
        logger.setLevel(logging.DEBUG)

        # Adicionando identificador de execução à data e hora atual
        exec_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, f'exec_id_{exec_id}.txt')

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger

    def build_service(self):
        creds = self.get_credentials()
        return build('calendar', 'v3', credentials=creds)

    def get_credentials(self):
        creds = None
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file)
        if not creds or not creds.valid:
            creds = self.refresh_credentials(creds)
        return creds

    def refresh_credentials(self, creds):
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.scopes)
            creds = flow.run_local_server(port=0)
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        return creds

def get_user_choice():
    print("Escolha a ação desejada:")
    print("1. Solicitar agendamento")
    print("2. Desmarcar agendamento")
    print("3. Remarcar agendamento")
    
    choice = input("Digite o número da ação desejada: ")
    return choice

def get_action_params(choice):
    if choice == '1':
        return {}
    elif choice == '2':
        return {}  # Adicione lógica para obter parâmetros de desmarcação
    elif choice == '3':
        return {}  # Adicione lógica para obter parâmetros de remarcação
    else:
        print("Escolha inválida.")
        return None

def main():
    calendar_service = GoogleCalendarService()

    choice = get_user_choice()
    action_params = get_action_params(choice)

    if action_params is not None:
        strategy = RequestEventActionStrategy() if choice == '1' else CancelEventActionStrategy() if choice == '2' else RescheduleEventActionStrategy()
        context = EventProcessorContext(strategy)
        context.process_events(calendar_service, **action_params)

if __name__ == '__main__':
    main()
