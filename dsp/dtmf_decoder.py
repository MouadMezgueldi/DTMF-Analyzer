import numpy as np
from scipy.signal import find_peaks


class DTMFDecoder:

    def __init__(self, tol=20):

        self.low_freqs = np.array([697, 770, 852, 941])
        self.high_freqs = np.array([1209, 1336, 1477])

        self.touches = np.array([
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
            ['*','0','#']
        ])

        self.tol = tol


    def decode(self, freqs, spectrum):
        mask = freqs > 0
        f_pos = freqs[mask]
        A_pos = spectrum[mask]

        
        max_amplitude = np.max(A_pos)
        if max_amplitude < 0.01:  # Seuil minimal absolu
            return None

        
        threshold = 0.2 * max_amplitude  

        # Calculer la distance en termes d'indices
        freq_resolution = f_pos[1] - f_pos[0] if len(f_pos) > 1 else 10
        min_distance = int(80 / freq_resolution) if freq_resolution > 0 else 8
        
        # find_peaks avec prominence pour ignorer le bruit
        peaks, props = find_peaks(
            A_pos,
            height=threshold,
            distance=min_distance,
            prominence=threshold * 0.5  # detecte que les pics 50% plus proches à threshold
        )

        if len(peaks) < 2: # un cas où on a pas aucune combinaison valide
            return None


        peak_freqs = f_pos[peaks]
        
        # Filtrer les fréquences hors de la plage DTMF (600-1600 Hz)
        valid_mask = (peak_freqs >= 600) & (peak_freqs <= 1600)
        peak_freqs = peak_freqs[valid_mask]
        
        if len(peak_freqs) < 2:
            return None
        

        return self._find_dtmf(peak_freqs)


    def _find_dtmf(self, peak_freqs):

        n = len(peak_freqs)

        if n < 2:
            return None

        # Chercher une paire basse/haute valide
        best_match = None
        best_score = float('inf')
        
        for i in range(n-1):
            for j in range(i+1, n):

                f1 = peak_freqs[i]
                f2 = peak_freqs[j]

                key, score = self._match_freqs(f1, f2)

                if key is not None and score < best_score:
                    best_match = key
                    best_score = score

        return best_match


    def _match_freqs(self, f1, f2):

        f_low = min(f1, f2)
        f_high = max(f1, f2)

        # Vérifier que f_low est dans la plage basse et f_high dans la plage haute
        if f_low > 1000 or f_high < 1100:  # Séparation claire basse/haute
            return None, float('inf')

        diffL = np.abs(self.low_freqs - f_low)
        diffH = np.abs(self.high_freqs - f_high)

        idxL = np.argmin(diffL)
        idxH = np.argmin(diffH)

        if diffL[idxL] > self.tol:
            return None, float('inf')

        if diffH[idxH] > self.tol:
            return None, float('inf')

        # Retourner la touche et le score (somme des erreurs)
        score = diffL[idxL] + diffH[idxH]
        return self.touches[idxL, idxH], score
    