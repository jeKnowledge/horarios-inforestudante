class AulaDataRaw:
    def __init__(self, aulaId, aulaNome, aulaCodigo, semestre, turma, turmaCapacidade, turmaId, dataInicio, dataFim):
        self.aulaId = aulaId
        self.aulaNome = aulaNome
        self.aulaCodigo = aulaCodigo
        self.semestre = semestre
        self.turma = turma
        self.turmaCapacidade = turmaCapacidade
        self.turmaId = turmaId
        self.dataInicio = dataInicio
        self.dataFim = dataFim

class AulaDataSripped:
    def __init__(self, aulaId, semestre, turmaId, dia, horaInicio, horaFim):
        self.aulaId = aulaId
        self.semestre = semestre
        self.turmaId = turmaId
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFim = horaFim
    def dataStr(self):
        return "aulaId: " + str(self.aulaId) + "\nsemestre: " + str(self.semestre) + "\nturmaId: " + str(self.turmaId) + "\ndia: " + str(self.dia) + "\nhoraInicio: " + str(self.horaInicio) + "\nhoraFim: " + str(self.horaFim)